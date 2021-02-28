import random
import string

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QLabel, QComboBox, QPushButton, QLineEdit


class CreatePasswordWidget(QVBoxLayout):
    def __init__(self, *args, window):
        super().__init__(*args)
        self.window = window
        self.addObjectToLayout()

    def createWidget(self):
        self.groupBox = QGroupBox()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.labelNew = QLabel(self.window)
        self.labelNew.setText("Create new Password")
        self.labelNew.setFont(QtGui.QFont("Sanserif", 25))
        self.labelNew.setAlignment(Qt.AlignHCenter)
        gridLayout.addWidget(self.labelNew)

        vbox1 = QVBoxLayout()
        self.labelType = QLabel(self.window)
        self.labelType.setText("Type of password :")
        self.labelType.setFont(QtGui.QFont("Sanserif", 15))
        vbox1.addWidget(self.labelType, alignment=Qt.AlignBottom)

        self.comboBoxType = QComboBox(self.window)
        self.comboBoxType.setFont(QtGui.QFont("Sanserif", 15))
        self.comboBoxType.addItem("Website")
        vbox1.addWidget(self.comboBoxType, alignment=Qt.AlignTop)

        vbox2 = QVBoxLayout()
        self.labelWebsite = QLabel(self.window)
        self.labelWebsite.setText("Website :")
        self.labelWebsite.setFont(QtGui.QFont("Sanserif", 15))
        vbox2.addWidget(self.labelWebsite, alignment=Qt.AlignBottom)

        self.websiteValue = QLineEdit(self.window)
        self.websiteValue.setFont(QtGui.QFont("Sanserif", 15))
        self.websiteValue.textChanged.connect(self.checkAllValue)
        vbox2.addWidget(self.websiteValue, alignment=Qt.AlignTop)

        vbox3 = QVBoxLayout()
        vbox3.setStretch(1, 1)
        self.labelUsername = QLabel(self.window)
        self.labelUsername.setText("Username :")
        self.labelUsername.setFont(QtGui.QFont("Sanserif", 15))
        vbox3.addWidget(self.labelUsername, alignment=Qt.AlignBottom)

        self.usernameValue = QLineEdit(self.window)
        self.usernameValue.setFont(QtGui.QFont("Sanserif", 15))
        self.usernameValue.textChanged.connect(self.checkAllValue)
        vbox3.addWidget(self.usernameValue, alignment=Qt.AlignTop)

        vbox4 = QVBoxLayout()
        vbox4.setStretch(1, 1)
        self.labelPassword = QLabel(self.window)
        self.labelPassword.setText("Password :")
        self.labelPassword.setFont(QtGui.QFont("Sanserif", 15))
        vbox4.addWidget(self.labelPassword, alignment=Qt.AlignBottom)

        self.passwordValue = QLineEdit(self.window)
        self.passwordValue.setText(self.get_random_password(32))
        self.passwordValue.setFont(QtGui.QFont("Sanserif", 15))

        self.passwordValue.textChanged.connect(self.checkAllValue)
        vbox4.addWidget(self.passwordValue, alignment=Qt.AlignTop)

        self.buttonValidate = QPushButton(self.window)
        self.buttonValidate.setText("Validate User")
        self.buttonValidate.setFont(QtGui.QFont("Sanserif", 15))
        self.buttonValidate.setFixedHeight(50)
        self.buttonValidate.setFixedWidth(200)
        self.buttonValidate.setEnabled(False)
        self.buttonValidate.clicked.connect(self.savePassword)


        gridLayout.addLayout(vbox1, 2, 0)
        gridLayout.addLayout(vbox2, 3, 0)
        gridLayout.addLayout(vbox3, 4, 0)
        gridLayout.addLayout(vbox4, 5, 0)
        gridLayout.addWidget(self.buttonValidate, 6, 0)

        self.groupBox.setMaximumHeight(400)
        self.groupBox.setLayout(gridLayout)

    def addObjectToLayout(self):
        self.createWidget()
        self.addWidget(self.groupBox)


    def savePassword(self):
        password = "Website=!=" + str(self.websiteValue.text()) + "!?&User=!=" + str(self.usernameValue.text()) \
                   + "!?&Password=!=" + str(self.passwordValue.text())
        self.window.goToPasswordScreen(password=password, cryptFile=None, user=None)

    def checkAllValue(self):
        if len(self.websiteValue.text()) > 0 and len(self.usernameValue.text()) > 0 and len(self.passwordValue.text()):
            self.buttonValidate.setEnabled(True)
        else:
            self.buttonValidate.setEnabled(False)

    def get_random_password(self, size):
        source = string.ascii_letters + string.digits
        return ''.join((random.choice(source) for i in range(size)))