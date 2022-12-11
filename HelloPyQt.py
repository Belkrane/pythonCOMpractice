import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class baseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle("pyQt Practice")

        btn1 = QPushButton("Click", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_click)

        btn2 = QPushButton("Quit", self)
        btn2.move(20, 60)
        btn2.clicked.connect(QCoreApplication.instance().quit)

    
    def btn1_click(self):
        QMessageBox.about(self, "message", "button 1 Clicked!!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = baseWindow()
    window.show()
    app.exec_()

