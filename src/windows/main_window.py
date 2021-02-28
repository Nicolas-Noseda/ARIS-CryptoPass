import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from src.widgets.create_user_widget import CreateUserWidget
from src.widgets.login_widget import LoginWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, list_user):
        super().__init__(*args)
        self.list_user = list_user
        self.setupWindow()

    def setupWindow(self):
        self.setFixedWidth(600)
        self.setMinimumHeight(500)
        self.setWindowTitle("ARIS-CryptoPass")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + "images" + os.path.sep + "Icon_Head.png"))
        qtRectangle = self.frameGeometry()
        bottomRightPoint = QDesktopWidget().availableGeometry(screen=1).bottomRight()
        qtRectangle.moveBottomRight(bottomRightPoint)
        self.move(qtRectangle.topLeft())
        if len(self.list_user) > 0:
            self.useLoginUserLayout()
        else:
            self.useCreateUserLayout()

    def useLoginUserLayout(self):
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(LoginWidget(window=self, list_user=self.list_user))

    def useCreateUserLayout(self):
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(CreateUserWidget(window=self))

    def goToPasswordScreen(self, password, cryptFile):
        self.cryptFile = cryptFile
        self.password = password

