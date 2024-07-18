import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QComboBox, QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QCheckBox, QGridLayout, QMessageBox, QSpinBox
from albumentations import Compose, RandomRotate90, BboxParams, Blur ,RandomBrightnessContrast, RandomGamma, Sharpen, HorizontalFlip, VerticalFlip, CLAHE, HueSaturationValue, ShiftScaleRotate, RandomBrightness
import cv2
import json

class ImageAugmentationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selectedFolder = ''
        self.annotationFolder = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Augmentation Tool')
        self.setGeometry(100, 100, 800, 600)
        mainLayout = QVBoxLayout()

        # Layout for selecting image directory
        directoryLayout = QHBoxLayout()
        self.btnSelectFolder = QPushButton('Select Image Folder', self)
        self.btnSelectFolder.clicked.connect(self.openFolderDialog)
        mainLayout.addWidget(self.btnSelectFolder)

        # Checkbox for annotations
        self.cbAnnotations = QCheckBox('Check this if you have annotations', self)
        self.cbAnnotations.stateChanged.connect(self.annotationCheckboxChanged)
        mainLayout.addWidget(self.cbAnnotations)

        # Dropdown for annotation format
        self.annotationFormatDropdown = QComboBox(self)
        self.annotationFormatDropdown.addItem("YOLO (.txt)")
        self.annotationFormatDropdown.addItem("COCO (.json)")
        self.annotationFormatDropdown.setEnabled(False)
        mainLayout.addWidget(self.annotationFormatDropdown)

        # Layout for selecting annotation directory or file
        annotationLayout = QHBoxLayout()
        self.btnSelectAnnotationFolder = QPushButton('Select Annotations', self)
        self.btnSelectAnnotationFolder.clicked.connect(self.openAnnotationFolderDialog)
        self.btnSelectAnnotationFolder.setEnabled(False)
        annotationLayout.addWidget(self.btnSelectAnnotationFolder)
        mainLayout.addLayout(annotationLayout)

        # Grid layout for checkboxes (augmentation types)
        gridLayout = QGridLayout()
        self.setupCheckBoxes(gridLayout)
        mainLayout.addLayout(gridLayout)

        # Spin box for total desired images
        spinBoxLayout = QHBoxLayout()
        self.labelDesiredImages = QLabel('Total Desired Images:', self)
        self.spinBoxDesiredImages = QSpinBox(self)
        self.spinBoxDesiredImages.setRange(1, 1000)
        self.spinBoxDesiredImages.setValue(10)
        spinBoxLayout.addWidget(self.labelDesiredImages)
        spinBoxLayout.addWidget(self.spinBoxDesiredImages)
        mainLayout.addLayout(spinBoxLayout)

        # Augment Images button
        self.btnAugmentImages = QPushButton('Augment', self)
        self.btnAugmentImages.clicked.connect(self.augmentImages)
        mainLayout.addWidget(self.btnAugmentImages)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def setupCheckBoxes(self, gridLayout):
        self.cbRotate = QCheckBox('Rotate 90', self)
        self.cbFlipH = QCheckBox('Flip Horizontally', self)
        self.cbFlipV = QCheckBox('Flip Vertically', self)
        self.cbBlur = QCheckBox('Blur', self)
        self.cbSaturation = QCheckBox('Saturation', self)
        self.cbContrast = QCheckBox('Contrast', self)
        self.cbSharpness = QCheckBox('Sharpness', self)
        self.cbGamma = QCheckBox('Gamma', self)
        self.cbCLAHE = QCheckBox('CLAHE', self)
        self.cbHSV = QCheckBox('HSV', self)
        self.cbSSR = QCheckBox('Shift, Scale, Rotate', self)
        self.cbBrightness = QCheckBox('Brightness', self)

        gridLayout.addWidget(self.cbRotate, 0, 0)
        gridLayout.addWidget(self.cbFlipH, 0, 1)
        gridLayout.addWidget(self.cbFlipV, 0, 2)
        gridLayout.addWidget(self.cbBlur, 1, 0)
        gridLayout.addWidget(self.cbSaturation, 1, 1)
        gridLayout.addWidget(self.cbContrast, 1, 2)
        gridLayout.addWidget(self.cbSharpness, 1, 3)
        gridLayout.addWidget(self.cbGamma, 2, 0)
        gridLayout.addWidget(self.cbCLAHE, 2, 1)
        gridLayout.addWidget(self.cbHSV, 2, 2)
        gridLayout.addWidget(self.cbSSR, 2, 3)
        gridLayout.addWidget(self.cbBrightness, 0, 3)

    def annotationCheckboxChanged(self):
        if self.cbAnnotations.isChecked():
            self.annotationFormatDropdown.setEnabled(True)
            self.btnSelectAnnotationFolder.setEnabled(True)
        else:
            self.annotationFormatDropdown.setEnabled(False)
            self.btnSelectAnnotationFolder.setEnabled(False)

    def openFolderDialog(self):
        self.selectedFolder = QFileDialog.getExistingDirectory(self, "Select Image Directory")
        if not self.selectedFolder:
            QMessageBox.warning(self, "Selection Error", "No directory selected")

    def openAnnotationFolderDialog(self):
        annotation_format = self.annotationFormatDropdown.currentText()
        print(f"Selected annotation format: {annotation_format}")  # Debug print
        if annotation_format == "COCO":
            print("Expecting JSON file for COCO format")  # Debug print
            self.annotationFolder, _ = QFileDialog.getOpenFileName(self, "Select COCO Annotation File", "", "JSON Files (*.json)")
            if not self.annotationFolder:
                QMessageBox.warning(self, "Selection Error", "No file selected")
        else:
            self.annotationFolder = QFileDialog.getExistingDirectory(self, "Select Annotation Directory")
            if not self.annotationFolder:
                QMessageBox.warning(self, "Selection Error", "No directory selected")

    def augmentImages(self):
        if not self.selectedFolder:
            QMessageBox.critical(self, "Error", "Please select an image folder.")
            return

        selected_augmentations = {
            'rotate': self.cbRotate.isChecked(),
            'flip_h': self.cbFlipH.isChecked(),
            'flip_v': self.cbFlipV.isChecked(),
            'blur': self.cbBlur.isChecked(),
            'saturation': self.cbSaturation.isChecked(),
            'contrast': self.cbContrast.isChecked(),
            'sharpness': self.cbSharpness.isChecked(),
            'gamma': self.cbGamma.isChecked(),
            'clahe': self.cbCLAHE.isChecked(),
            'hsv': self.cbHSV.isChecked(),
            'ssr': self.cbSSR.isChecked(),
            'brightness': self.cbBrightness.isChecked()
        }
        total_desired_images = self.spinBoxDesiredImages.value()

        try:
            if self.cbAnnotations.isChecked():
                if not self.annotationFolder:
                    QMessageBox.critical(self, "Error", "Please select an annotation folder or file.")
                    return

                annotation_format = self.annotationFormatDropdown.currentText()
                print(f"Annotation format in augmentImages: {annotation_format}")  # Debug print
                if annotation_format == "COCO":
                    augment_images_in_folder_coco(self.selectedFolder, self.annotationFolder, total_desired_images, selected_augmentations)
                else:
                    augment_images_in_folder_yolo(self.selectedFolder, self.annotationFolder, total_desired_images, selected_augmentations)
            else:
                augment_images_only(self.selectedFolder, total_desired_images, selected_augmentations)

            QMessageBox.information(self, "Success", "Images have been augmented. Check the 'augmented' folder.")
        except Exception as e:
            QMessageBox.critical(self, "Error during augmentation", f"{str(e)}")
            print(f"Error during augmentation: {str(e)}")

def main():
    app = QApplication(sys.argv)
    ex = ImageAugmentationApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
