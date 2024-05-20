# user_profile.py
# import neccessary modules
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self) -> None:
        """ Set up the GUI for the application """
        self.setFixedHeight(350)
        self.setFixedWidth(300)
        self.setGeometry(100, 250, 250, 400)
        self.setWindowTitle("User Profile Example")

        self.setUpMainWindow()
        self.show()

    def createImageLabels(self) -> None:
        """ Open image fies and create image labels """
        images: list[str] = ['PyQt/images/skyblue.png', 'PyQt/images/profile_image.png']
        for image in images:
            try:
                with open(image):
                    label: QLabel = QLabel(self)
                    pixmap: QPixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                if image == 'PyQt/images/profile_image.png':
                    # label.resize(400, 400)
                    label.move(15, 30)
                    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")

    def setUpMainWindow(self) -> None:
        """ Create QLabel to be displayed in the main window """
        self.createImageLabels()
        # set the name label and its font
        user_label: QLabel = QLabel(self)
        user_label.setText("Xuhua Huang")
        user_label.setFont(QFont("Arial", 20))

        # set the bio label and its font
        bio_label: QLabel = QLabel(self)
        bio_label.setText("std::code_blooded")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 180)

        # create the brief description label
        about_label: QLabel = QLabel(self)
        about_label.setText("Strong passion in Embedded Software Development w/ C/C++, Python & Rust")
        bio_label.setFont(QFont("Arial", 13))
        about_label.setWordWrap(True)
        about_label.move(15, 200)

        # add more labels to the method
        languages_label: QLabel = QLabel(self)
        languages_label.setText("C | C++ | Rust | Python")
        languages_label.move(15, 230)


# Run the program
if __name__ == '__main__':
    # Create QApplication object
    app = QApplication(sys.argv)
    # Create window from QWidget object
    window = MainWindow()
    # Start the event loop, and use sys.exit to close the program
    sys.exit(app.exec())
