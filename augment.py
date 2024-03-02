from torchvision import transforms
from PIL import Image
import os
import random

def get_transform():
    # Define a set of transformations for augmentation with less intense rotations
    transform = transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.3),  # Flips the image horizontally with a probability of 0.5
        transforms.RandomVerticalFlip(p=0.2),  # Flips the image vertically with a probability of 0.5
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.02),  # Slight color jitter
        transforms.RandomRotation(degrees=(-30, 30)),  # Limits the rotation to +/- 30 degrees
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1), shear=10),  # Affine transformation without rotation
        transforms.RandomPerspective(distortion_scale=0.5, p=0.5),  # Random perspective transformation
        transforms.RandomGrayscale(p=0.1),  # Converts the image to grayscale with a probability of 0.1
        transforms.GaussianBlur(kernel_size=3, sigma=(0.1, 2.0)),  # Applies Gaussian blur
    ])
    return transform

def augment_image(image_path, save_dir, transform, count):
    image = Image.open(image_path)
    augmented_image = transform(image)
    
    # Using the count to ensure unique file names
    save_path = os.path.join(save_dir, f'aug_{count}_{os.path.basename(image_path)}')
    augmented_image.save(save_path)

def augment_images_in_folder(folder_path, total_desired_images):
    original_images = [img for img in os.listdir(folder_path) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
    num_original_images = len(original_images)
    if num_original_images == 0:
        raise Exception("No images found in the folder.")

    augmentations_needed = total_desired_images - num_original_images
    if augmentations_needed <= 0:
        raise Exception("The folder already contains the desired number of images or more.")

    save_dir = os.path.join(folder_path, 'augmented')
    os.makedirs(save_dir, exist_ok=True)

    transform = get_transform()

    for count in range(augmentations_needed):
        # Cycle through original images for augmentation
        image_name = original_images[count % num_original_images]
        image_path = os.path.join(folder_path, image_name)
        augment_image(image_path, save_dir, transform, count)
