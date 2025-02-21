import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import test_ui


class testGUI(QMainWindow, test_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setButton.clicked.connect(self.set)
        self.clearButton.clicked.connect(self.clear)

    def set(self):
        self.label.setText("Hello")

    def clear(self):
        self.label.setText("")

def main():
    app = QApplication(sys.argv)
    gui = testGUI()

    gui.show()
    app.exec_()

if __name__ == '__main__':
    main()
