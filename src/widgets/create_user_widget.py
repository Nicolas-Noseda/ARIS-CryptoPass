from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLineEdit, QLabel

from src.classes.files_management import create_new_files


class CreateUserWidget(QVBoxLayout):
    def __init__(self, *args, window):
        super().__init__(*args)
        self.window = window
        self.addObjectToLayout()

    def createLayout(self):
        self.groupBox = QGroupBox()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.labelCreate = QLabel(self.window)
        self.labelCreate.setText("Create User to store Password")
        self.labelCreate.setFont(QtGui.QFont("Sanserif", 25))
        self.labelCreate.setAlignment(Qt.AlignHCenter)
        gridLayout.addWidget(self.labelCreate)

        vbox1 = QVBoxLayout()
        self.labelUser = QLabel(self.window)
        self.labelUser.setText("Username :")
        self.labelUser.setFont(QtGui.QFont("Sanserif", 15))
        vbox1.addWidget(self.labelUser, alignment=Qt.AlignBottom)

        self.lineEditUser = QLineEdit(self.window)
        self.lineEditUser.setFont(QtGui.QFont("Sanserif", 15))
        self.lineEditUser.textChanged.connect(self.checkUser)
        vbox1.addWidget(self.lineEditUser, alignment=Qt.AlignTop)

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

        self.buttonValidate = QPushButton(self.window)
        self.buttonValidate.setText("Create the user")
        self.buttonValidate.setFont(QtGui.QFont("Sanserif", 15))
        self.buttonValidate.setFixedHeight(50)
        self.buttonValidate.setFixedWidth(200)
        self.buttonValidate.setEnabled(False)
        self.buttonValidate.clicked.connect(self.createUser)

        gridLayout.addLayout(vbox1, 1, 0)
        gridLayout.addLayout(vbox2, 2, 0)

        gridLayout.addWidget(self.buttonValidate, 3, 0, alignment=Qt.AlignCenter)

        self.labelError = QLabel(self.window)
        self.labelError.setText("You have to create passphrase of 30 character minimum, it's for you're own safety ;)")
        self.labelError.setFont(QtGui.QFont("Sanserif", 10, weight=QtGui.QFont.Bold))
        self.labelError.setWordWrap(True)
        self.labelError.setStyleSheet("QLabel {color: red}")

        self.labelError.setHidden(True)
        gridLayout.addWidget(self.labelError, 4, 0)

        self.groupBox.setMaximumHeight(400)
        self.groupBox.setLayout(gridLayout)

    def addObjectToLayout(self):
        self.createLayout()
        self.addWidget(self.groupBox)

    def createUser(self):
        print(str(self.lineEditUser.text()))
        print(str(self.passPhrase.text()))
        create_new_files(user=str(self.lineEditUser.text()))

    def checkUser(self):
        if len(self.lineEditUser.text()) > 0 and len(self.passPhrase.text()) > 30:
            self.buttonValidate.setEnabled(True)
        else:
            self.buttonValidate.setEnabled(False)

    def checkPassPhrase(self):
        if len(self.passPhrase.text()) > 30:
            self.labelError.setHidden(True)
            self.buttonValidate.setEnabled(True)
        else:
            self.labelError.setHidden(False)
            self.buttonValidate.setEnabled(False)


