from torchvision import transforms
from PIL import Image
import os

def get_transform(selected_augmentations):
    transformations = []
    # Basic transformations
    if selected_augmentations.get('rotation'):
        transformations.append(transforms.RandomRotation(degrees=(0, 360)))
    if selected_augmentations.get('flip'):
        transformations.append(transforms.RandomHorizontalFlip())
        transformations.append(transforms.RandomVerticalFlip())
    if selected_augmentations.get('blur'):
        transformations.append(transforms.GaussianBlur(5))
    if selected_augmentations.get('saturation'):
        transformations.append(transforms.ColorJitter(saturation=2))
    
    # Advanced transformations
    if selected_augmentations.get('contrast'):
        transformations.append(transforms.ColorJitter(contrast=2))
    if selected_augmentations.get('sharpness'):
        transformations.append(transforms.RandomAdjustSharpness(2))
    if selected_augmentations.get('random_crop'):
        transformations.append(transforms.RandomResizedCrop(224))
    if selected_augmentations.get('random_erase'):
        transformations.append(transforms.RandomErasing())
    if selected_augmentations.get('affine'):
        transformations.append(transforms.RandomAffine(degrees=(0, 360)))

    # Additional transformations
    if selected_augmentations.get('grayscale'):
        transformations.append(transforms.RandomGrayscale())
    if selected_augmentations.get('perspective'):
        transformations.append(transforms.RandomPerspective())
    if selected_augmentations.get('color_jitter'):
        transformations.append(transforms.ColorJitter())
    if selected_augmentations.get('equalize'):
        transformations.append(transforms.RandomEqualize())
    if selected_augmentations.get('invert'):
        transformations.append(transforms.RandomInvert())

    transform = transforms.Compose(transformations)
    return transform

def augment_image(image_path, save_dir, transform, count):
    image = Image.open(image_path)
    augmented_image = transform(image)
    save_path = os.path.join(save_dir, f'aug_{count}_{os.path.basename(image_path)}')
    augmented_image.save(save_path)

def augment_images_in_folder(folder_path, total_desired_images, selected_augmentations):
    original_images = [img for img in os.listdir(folder_path) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
    num_original_images = len(original_images)
    if num_original_images == 0:
        raise Exception("No images found in the folder.")

    augmentations_needed = total_desired_images - num_original_images
    if augmentations_needed <= 0:
        raise Exception("The folder already contains the desired number of images or more.")

    save_dir = os.path.join(folder_path, 'augmented')
    os.makedirs(save_dir, exist_ok=True)

    transform = get_transform(selected_augmentations)

    for count in range(augmentations_needed):
        image_name = original_images[count % num_original_images]
        image_path = os.path.join(folder_path, image_name)
        augment_image(image_path, save_dir, transform, count)
