import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLineEdit, QLabel, QComboBox, QHBoxLayout
from cryptography.fernet import InvalidToken

from src.classes.crypto import CryptFile


class LoginWidget(QVBoxLayout):
    def __init__(self, *args, window, list_user):
        super().__init__(*args)
        self.attemptToConnect = 0
        self.window = window
        self.list_user = list_user
        self.addObjectToLayout()

    def createLayout(self):
        self.groupBox = QGroupBox()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.labelLogin = QLabel(self.window)
        self.labelLogin.setText("Access to your Password")
        self.labelLogin.setFont(QtGui.QFont("Sanserif", 25))
        self.labelLogin.setAlignment(Qt.AlignHCenter)
        gridLayout.addWidget(self.labelLogin)

        vbox1 = QVBoxLayout()
        self.labelUser = QLabel(self.window)
        self.labelUser.setText("Username :")
        self.labelUser.setFont(QtGui.QFont("Sanserif", 15))
        vbox1.addWidget(self.labelUser, alignment=Qt.AlignBottom)

        self.comboBoxUser = QComboBox(self.window)
        self.comboBoxUser.setFont(QtGui.QFont("Sanserif", 15))
        for user in self.list_user:
            self.comboBoxUser.addItem(user)
        vbox1.addWidget(self.comboBoxUser, alignment=Qt.AlignTop)

        vbox2 = QVBoxLayout()
        vbox2.setStretch(1, 1)
        self.labelPassPhrase = QLabel(self.window)
        self.labelPassPhrase.setText("Enter your passphrase :")
        self.labelPassPhrase.setFont(QtGui.QFont("Sanserif", 15))
        vbox2.addWidget(self.labelPassPhrase, alignment=Qt.AlignBottom)

        self.passPhrase = QLineEdit(self.window)
        self.passPhrase.setFont(QtGui.QFont("Sanserif", 15))
        self.passPhrase.setEchoMode(QLineEdit.Password)
        self.passPhrase.textChanged.connect(self.checkPassPhrase)
        vbox2.addWidget(self.passPhrase, alignment=Qt.AlignTop)

        hbox = QHBoxLayout()
        self.buttonCreateUser = QPushButton(self.window)
        self.buttonCreateUser.setText("Create User")
        self.buttonCreateUser.setFont(QtGui.QFont("Sanserif", 15))
        self.buttonCreateUser.setFixedHeight(50)
        self.buttonCreateUser.setFixedWidth(200)
        self.buttonCreateUser.clicked.connect(self.goToCreateUserScreen)
        hbox.addWidget(self.buttonCreateUser)

        self.buttonValidate = QPushButton(self.window)
        self.buttonValidate.setText("Validate User")
        self.buttonValidate.setFont(QtGui.QFont("Sanserif", 15))
        self.buttonValidate.setFixedHeight(50)
        self.buttonValidate.setFixedWidth(200)
        self.buttonValidate.setEnabled(False)
        self.buttonValidate.clicked.connect(self.goToPasswordScreen)
        hbox.addWidget(self.buttonValidate)

        self.labelError = QLabel(self.window)
        self.labelError.setText("The passphrase is 30 character minimum")
        self.labelError.setFont(QtGui.QFont("Sanserif", 10, weight=QtGui.QFont.Bold))
        self.labelError.setWordWrap(True)
        self.labelError.setStyleSheet("QLabel {color: red}")

        gridLayout.addLayout(vbox1, 2, 0)
        gridLayout.addLayout(vbox2, 3, 0)

        gridLayout.addLayout(hbox, 5, 0)

        gridLayout.addWidget(self.labelError, 4, 0)

        self.groupBox.setMaximumHeight(400)
        self.groupBox.setLayout(gridLayout)

    def addObjectToLayout(self):
        self.createLayout()
        self.addWidget(self.groupBox)

    def goToPasswordScreen(self):
        cryptFile = CryptFile(str(self.passPhrase.text()))
        try:
            password = cryptFile.decrypt_file(str(self.comboBoxUser.currentText()))
            self.window.goToPasswordScreen(password, cryptFile, user=str(self.comboBoxUser.currentText()))
        except InvalidToken as e:
            if self.attemptToConnect < 5:
                self.attemptToConnect += 1
                self.labelError.setText("The passphrase is not good ! Attempt " + str(self.attemptToConnect) + "/5")
                self.passPhrase.setText("")
                self.labelError.setHidden(False)
                self.buttonValidate.setEnabled(False)
            else:
                sys.exit()
        except ValueError as e:
            self.window.goToPasswordScreen('', cryptFile, user=str(self.comboBoxUser.currentText()))

    def goToCreateUserScreen(self):
        self.window.useCreateUserLayout()

    def checkPassPhrase(self):
        if len(self.passPhrase.text()) > 30:
            self.labelError.setHidden(True)
            self.buttonValidate.setEnabled(True)
        else:
            self.labelError.setHidden(False)
            self.buttonValidate.setEnabled(False)