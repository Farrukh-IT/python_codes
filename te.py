import sys
from PyQt5 import QtWidgets

def Panjara():
    app = QtWidgets.QApplication(sys.argv)
    panjara =QtWidgets.QWidget()
    panjara.setWindowTitle("MY Applacation :)")
    panjara.show()
    sys.exit(app.exec_()) 

Panjara()
