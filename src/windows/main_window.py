import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from src.widgets.create_password_widget import CreatePasswordWidget
from src.widgets.create_user_widget import CreateUserWidget
from src.widgets.login_widget import LoginWidget
from src.widgets.password_screen_widget import PasswordScreenWidget


class MainWindow(QMainWindow):

    def __init__(self, *args, list_user):
        super().__init__(*args)
        self.list_user = list_user
        self.password = ""
        self.user = ""
        self.cryptFile = None
        self.setupWindow()

    def setupWindow(self):
        self.setFixedWidth(600)
        self.setFixedHeight(500)
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

    def goToPasswordScreen(self, password, cryptFile, user):
        if self.user == "":
            self.user = user

        if self.cryptFile is None:
            self.cryptFile = cryptFile

        if self.password == "" and password != "":
            self.password = password
            self.cryptFile.encrypt_file(self.password, self.user)
        elif password != "":
            self.password += ";!&?;" + password
            self.cryptFile.encrypt_file(self.password, self.user)

        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(PasswordScreenWidget(window=self, passwordList=self.password, cryptFile=self.cryptFile))

    def goToCreateNewPassword(self):
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(CreatePasswordWidget(window=self))

    def deletePasswordFromPasswordList(self, passwordToDelete):
        print(passwordToDelete)
        passwordtoSave = ""
        password_split = self.password.split(";!&?;")
        for password in password_split:
            if password != passwordToDelete:
                if passwordtoSave == "":
                    passwordtoSave += password
                else:
                    passwordtoSave += ";!&?;" + password
        self.cryptFile.encrypt_file(passwordtoSave, self.user)
        self.password = passwordtoSave
        self.goToPasswordScreen("", None, "")