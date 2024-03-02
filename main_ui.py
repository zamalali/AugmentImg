from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget)
import sys
import os
from augment import augment_images_in_folder

class ImageAugmentationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selectedFolder = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Augmentation Tool')

        self.setGeometry(100, 100, 800, 400)
        mainLayout = QVBoxLayout()
        
        # Label to show the selected directory and image count
        self.labelDirectory = QLabel('Select an image directory')
        mainLayout.addWidget(self.labelDirectory)
        
        self.labelCount = QLabel('Image Count: 0')
        mainLayout.addWidget(self.labelCount)

        # Horizontal layout for folder selection and image count
        directoryLayout = QHBoxLayout()
        self.btnSelectFolder = QPushButton('Select Folder', self)
        self.btnSelectFolder.clicked.connect(self.openFolderDialog)
        directoryLayout.addWidget(self.btnSelectFolder)

        mainLayout.addLayout(directoryLayout)

        # Horizontal layout for desired image count input
        countLayout = QHBoxLayout()
        self.labelDesiredCount = QLabel('Desired Image Count:')
        countLayout.addWidget(self.labelDesiredCount)

        self.inputDesiredCount = QLineEdit(self)
        countLayout.addWidget(self.inputDesiredCount)

        mainLayout.addLayout(countLayout)

        # Augment Images button
        self.btnAugmentImages = QPushButton('Augment Images', self)
        self.btnAugmentImages.clicked.connect(self.augmentImages)
        mainLayout.addWidget(self.btnAugmentImages)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def openFolderDialog(self):
        self.selectedFolder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if self.selectedFolder:
            self.labelDirectory.setText(f'Selected Folder: {self.selectedFolder}')
            self.updateImageCount()

    def updateImageCount(self):
        image_files = [img for img in os.listdir(self.selectedFolder) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
        self.labelCount.setText(f'Image Count: {len(image_files)}')

    def augmentImages(self):
        if not self.selectedFolder or self.selectedFolder.startswith('Select an image directory'):
            self.labelDirectory.setText('Please select a folder first.')
            return

        try:
            desired_count = int(self.inputDesiredCount.text())
            augment_images_in_folder(self.selectedFolder, desired_count)
            self.labelDirectory.setText(f'Images have been augmented. Check the "augmented" folder within {self.selectedFolder}.')
            self.updateImageCount()  # Update count after augmentation
        except ValueError:
            self.labelDirectory.setText('Please enter a valid number for desired image count.')
        except Exception as e:
            self.labelDirectory.setText(f'Error during augmentation: {e}')

def main():
    app = QApplication(sys.argv)
    ex = ImageAugmentationApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
