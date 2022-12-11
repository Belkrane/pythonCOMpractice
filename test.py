import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

label = QLabel("test")

label.show()
app.exec_()