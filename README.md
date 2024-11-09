# AugmentImg 📚
 
AugmentImg is a user-friendly image augmentation tool for computer vision tasks. It offers a no-code graphical interface to apply various augmentations to images and their annotations. Simply input the desired count and select the types of augmentations. It supports both YOLO (txt) and COCO (json) annotation formats. <br>
Leave a star before you leave ⭐

[![PyPI](https://img.shields.io/pypi/v/augmentimg)](https://pypi.org/project/augmentimg/)
[![Language](https://img.shields.io/badge/lang-en-blue.svg)](#)
![PyPI Downloads](https://static.pepy.tech/badge/augmentimg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### You can install this using [pip](https://pypi.org/project/augmentimg/)

### Here's how AugmentImg is used


<div align="center">
  <img src="https://raw.githubusercontent.com/zamalali/AugmentImg/main/images/MyYoutube.gif" alt="User Interface">
</div>

## Features

- **Supports image augmentation with YOLO and COCO annotation formats.**
- **Apply multiple augmentations like Rotation, Flip, Blur, Saturation, Contrast, Sharpness, Gamma correction, CLAHE, HSV adjustment, shift-scale-rotate, and Brightness.**
- **Easy to use GUI.**
- **Allows selection of the desired number of augmented images.**
- **Options to augment images with or without annotations.**


Checklist for Image Transformations
====================================

In the Image Augmentation Tool, users have the flexibility to select specific image transformations they wish to apply to their images. This feature is implemented through a user-friendly checklist within the graphical user interface (GUI), enabling tailored augmentation processes according to user preferences. 

**Implementation Overview**:

The checklist is realized using PyQt5's `QCheckBox` widgets, each representing a different image transformation available in the torchvision library. Users can select or deselect these checkboxes to indicate which transformations they want to apply.

**Available Transformations**:

The tool provides a comprehensive set of image transformations, including but not limited to:

- **Rotation**: Rotate the image by a specified degree.
- **Flip**: Flip the image horizontally or vertically.
- **Blur**: Apply a Gaussian blur to the image.
- **Saturation**: Adjust the image's color saturation.
- **Contrast**: Modify the image's contrast level.
- **Sharpness**: Enhance or reduce the sharpness of the image.
- **Random Crop**: Crop random parts of the image.
- **Random Erase**: Randomly erase parts of the image.
- **Affine Transformations**: Apply affine transformations like scaling, translations, and rotations.

**How to Use the Checklist**:

1. **Select Folder**: Initially, users must select the folder containing the images they wish to augment.
2. **Choose Transformations**: Users can then go through the checklist and select the transformations they desire by clicking on the corresponding checkboxes.
3. **Specify Desired Image Count**: Users should enter the desired total count of images (original + augmented) in the provided input field.
4. **Augment Images**: By clicking the "Augment Images" button, the application will apply the selected transformations to the images in the chosen folder, generating augmented images until the desired count is reached.

**Technical Details**:

Upon initiating the augmentation process, the application dynamically constructs a transformation pipeline based on the selected options. This pipeline is then applied to each selected image, creating augmented versions which are saved to a designated subfolder within the original image directory.

This checklist approach not only enhances the tool's usability by providing control over the augmentation process but also allows for a wide range of augmentation combinations, catering to diverse requirements and preferences.

**Note**: The actual transformations applied may slightly vary depending on the specific settings and parameters chosen for each transformation type. You can still change them manually in augment.py file based on your requirements.

**For further information, please refer to the [documentation](docs/docs.rst) and if you are facing any issues you can refer to the possible [Img-not-supported](docs/errors.rst) error**


## Installation

Otherwise run the following commands in your terminal
```bash
pip install augmentimg
augment-img
```
Ensure you have Python 3.6+ installed, then clone the repository and install dependencies:

```bash
git clone https://github.com/zamalali/AugmentImg.git
cd AugmentImg
pip install -r requirements.txt
```
