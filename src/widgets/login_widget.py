from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLineEdit, QLabel, QTextEdit, QComboBox


class LoginWidget(QVBoxLayout):
    def __init__(self, *args, window, list_user):
        super().__init__(*args)
        self.addObjectToLayout(window, list_user)

    def createLayout(self, window, list_user):
        self.groupBox = QGroupBox()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        vbox1 = QVBoxLayout()
        self.labelUser = QLabel(window)
        self.labelUser.setText("Username :")
        self.labelUser.setFont(QtGui.QFont("Sanserif", 15))
        vbox1.addWidget(self.labelUser, alignment=Qt.AlignBottom)

        self.comboBoxUser = QComboBox(window)
        self.comboBoxUser.setFont(QtGui.QFont("Sanserif", 15))
        for user in list_user:
            self.comboBoxUser.addItem(user)
        vbox1.addWidget(self.comboBoxUser, alignment=Qt.AlignTop)

        vbox2 = QVBoxLayout()
        vbox2.setStretch(1, 1)
        self.labelPassPhrase = QLabel(window)
        self.labelPassPhrase.setText("Enter your passphrase :")
        self.labelPassPhrase.setFont(QtGui.QFont("Sanserif", 15))
        vbox2.addWidget(self.labelPassPhrase, alignment=Qt.AlignBottom)

        self.passPhrase = QLineEdit(window)
        self.passPhrase.setFont(QtGui.QFont("Sanserif", 15))
        self.passPhrase.setEchoMode(QLineEdit.Password)
        vbox2.addWidget(self.passPhrase, alignment=Qt.AlignTop)

        self.buttonValidate = QPushButton(window)
        self.buttonValidate.setText("Validate")
        self.buttonValidate.setFont(QtGui.QFont("Sanserif", 15))
        self.buttonValidate.setBaseSize(100, 50)

        gridLayout.addLayout(vbox1, 1, 0)
        gridLayout.addLayout(vbox2, 2, 0)

        gridLayout.addWidget(self.buttonValidate, 3, 0)

        self.groupBox.setMaximumHeight(400)
        self.groupBox.setLayout(gridLayout)


    def addObjectToLayout(self, window, list_user):
        self.createLayout(window, list_user)
        self.addWidget(self.groupBox)