import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget


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
