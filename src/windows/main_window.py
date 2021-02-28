import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QVBoxLayout

from src.widgets.login_widget import LoginWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, mode=None):
        super().__init__(*args)
        self.mode = mode
        self.setupWindow()

    def setupWindow(self):
        self.setFixedWidth(600)
        self.setMinimumHeight(700)
        self.setWindowTitle("ARIS-CryptoPass")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + "images" + os.path.sep + "Icon_Head.png"))
        qtRectangle = self.frameGeometry()
        bottomRightPoint = QDesktopWidget().availableGeometry(screen=1).bottomRight()
        qtRectangle.moveBottomRight(bottomRightPoint)
        self.move(qtRectangle.topLeft())
        self.createLoginLayout()

    def createLoginLayout(self):
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        list_user = []
        list_user.append("User1")
        list_user.append("User2")
        list_user.append("User3")
        wid.setLayout(LoginWidget(window=self, list_user=list_user))

