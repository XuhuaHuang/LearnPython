# basic_window.py
# import neccessary modules
import sys
from PyQt6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):

    def __init__(self):
        """ Constructor for EmptyWindow class """
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application """
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty Window in PyQt")
        self.show()  # Display the window on the screen


# Run the program
if __name__ == '__main__':
    # Create QApplication object
    app = QApplication(sys.argv)
    # Create window from QWidget object
    window = EmptyWindow()
    # Start the event loop, and use sys.exit to close the program
    sys.exit(app.exec())
