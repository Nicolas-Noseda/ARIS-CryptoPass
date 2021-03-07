import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QSystemTrayIcon, QMenu, QAction

from src.classes import app
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
        self.tray = None
        self.setupWindow()

    def setupWindow(self):
        self.setFixedWidth(600)
        self.setFixedHeight(500)
        self.setWindowTitle("ARIS-CryptoPass")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + "images" + os.path.sep + "Icon_Head.png"))
        qtRectangle = self.frameGeometry()
        bottomRightPoint = QDesktopWidget().availableGeometry(screen=0).bottomRight()
        qtRectangle.moveBottomRight(bottomRightPoint)
        self.move(qtRectangle.topLeft())
        if len(self.list_user) > 0:
            self.useLoginUserLayout()
        else:
            self.useCreateUserLayout()

    def closeEvent(self, event):
        self.addTrayIcon()
        self.hide()
        self.setVisible(False)
        event.ignore()

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() == Qt.WindowMinimized:
                self.closeEvent(event)

    def addTrayIcon(self):
        if self.tray == None:
            self.tray = QSystemTrayIcon()
            scriptDir = os.path.dirname(os.path.realpath(__file__))
            self.tray.setIcon(QIcon(scriptDir + os.path.sep + "images" + os.path.sep + "Icon_Head.png"))
            self.tray.setToolTip("ARIS-CryptoPass")
            self.tray.activated.connect(self.trayIconClick)
            self.menu = QMenu()
            self.openAction = QAction("Open ARIS-CryptoPass")
            self.openAction.triggered.connect(self.reopenWindow)
            self.menu.addAction(self.openAction)
            self.exitAction = QAction("Close ARIS-CryptoPass")
            self.exitAction.triggered.connect(self.quitApp)
            self.menu.addAction(self.exitAction)
            self.tray.setContextMenu(self.menu)
            self.tray.show()
        else:
            self.tray.show()
            self.tray.setVisible(True)
        self.tray.showMessage("ARIS-CrytoPass",
                              "The app is still running, left-click to reopen, right-click to access menu")

    def quitApp(self):
        app.get_app().quit()

    def reopenWindow(self):
        self.show()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setVisible(True)
        self.tray.hide()
        self.tray.setVisible(False)

    def trayIconClick(self, reason):
        if reason == 3:
            self.reopenWindow()

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