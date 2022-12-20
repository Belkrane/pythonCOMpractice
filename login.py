import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 300, 150)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        btn1 = QPushButton("Login", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.login_clicked)

        btn2 = QPushButton("Check state", self)
        btn2.move(20, 70)
        btn2.clicked.connect(self.statusCheck_clicked)
    
    def login_clicked(self):
        ret = self.kiwoom.dynamicCall("CommConnect()")
        print(ret)

    def statusCheck_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()") == 0:
            print(self.kiwoom.dynamicCall("GetConnectState()"))
            self.statusBar().showMessage("Not Connected")
        else:
            print(self.kiwoom.dynamicCall("GetConnectState()"))
            self.statusBar().showMessage("Connected")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = BaseWindow()
    myWindow.show()
    app.exec_()
