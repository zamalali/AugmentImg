AugmentPy 📚
=========

AugmentPy is an open-source, Python-based tool crafted to augment image datasets by applying a wide array of transformations. It aims to enrich machine learning datasets with varied data, enhancing model robustness without changing the original image sizes.

Features
--------

- **Intuitive Graphical Interface**: Leveraging PyQt5, AugmentPy offers a straightforward GUI, making it accessible for both technical and non-technical users.
- **Diverse Augmentation Suite**: Includes horizontal and vertical flips, color jittering, rotations, and more, ensuring a broad spectrum of image variations.
- **Preservation of Image Integrity**: Augments images without resizing, maintaining the original dimensions and quality of the data.
- **Support for Common Image Formats**: Compatible with popular formats like PNG, JPEG, TIFF, BMP, and GIF, catering to a wide range of use cases.

Installation
------------

Ensure you have Python 3.6 or newer installed. Follow these steps to set up AugmentPy:

1. Clone the repository:

.. code-block:: bash

   git clone https://github.com/zamalali/AugmentPy.git
   cd AugmentPy

2. Install the necessary dependencies:

.. code-block:: bash

   pip install -r requirements.txt

Usage
-----

1. Launch AugmentPy:

.. code-block:: bash

   python main_ui.py

2. The GUI will prompt you to select an image folder. After selection, it displays the current image count.

3. Input the desired total number of images in the designated field.

4. Initiate the augmentation process by clicking on "Augment Images". Augmented images are saved in a subdirectory named `augmented` within the selected folder.

Supported Image Formats
-----------------------

AugmentPy works seamlessly with the following image extensions:

- .png
- .jpg, .jpeg
- .tiff
- .bmp

Customizing Augmentations
-------------------------

Adjust the `get_transform` function in `augment.py` to tailor the augmentation process to your specific needs, adding or removing transformations as required.

Contributing
------------

We welcome contributions to AugmentPy! Please refer to the CONTRIBUTING.rst file for guidelines on how to contribute effectively.

License
-------

AugmentPy is made available under the MIT License. See the LICENSE file in the repository for complete details.

Acknowledgments
---------------

Our heartfelt thanks to the PyTorch and PyQt communities for their invaluable resources that have significantly contributed to the development of AugmentPy.
