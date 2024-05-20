# labels.py
# import neccessary modules
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self) -> None:
        """ Set up the GUI for the application """
        self.setFixedHeight(500)
        self.setFixedWidth(450)
        self.setGeometry(100, 250, 250, 350)
        self.setWindowTitle("QLabel Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self) -> None:
        """ Create QLabel to be displayed in the main window """
        hello_label: QLabel = QLabel(self)
        hello_label.setText("Hello")
        hello_label.move(210, 15)

        image: str = './PyQt/images/world.png'
        try:
            with open(image):
                world_label: QLabel = QLabel(self)
                pixmap: QPixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


# Run the program
if __name__ == '__main__':
    # Create QApplication object
    app = QApplication(sys.argv)
    # Create window from QWidget object
    window = MainWindow()
    # Start the event loop, and use sys.exit to close the program
    sys.exit(app.exec())
