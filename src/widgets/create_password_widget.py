import random
import string

from PyQt5 import QtGui, sip
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QLabel, QComboBox, QPushButton, QLineEdit


class CreatePasswordWidget(QVBoxLayout):
    def __init__(self, *args, window):
        super().__init__(*args)
        self.window = window
        self.textType = "Website"
        self.addObjectToLayout()


    def createWidget(self):
        self.groupBoxWaou = self.createPasswordForm()

    def addObjectToLayout(self):
        self.createWidget()
        self.addWidget(self.groupBoxWaou)

    def createPasswordForm(self):
        groupBox = QGroupBox()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.labelNew = QLabel(self.window)
        self.labelNew.setText("Create new Password")
        self.labelNew.setFont(QtGui.QFont("Sanserif", 25))
        self.labelNew.setAlignment(Qt.AlignHCenter)
        gridLayout.addWidget(self.labelNew)

        vbox1 = QVBoxLayout()
        self.comboBoxType = QComboBox(self.window)
        self.comboBoxType.setFont(QtGui.QFont("Sanserif", 15))
        self.comboBoxType.addItem("Website")
        self.comboBoxType.addItem("Credit Cards")
        self.comboBoxType.currentTextChanged.connect(self.changedTextType)
        vbox1.addWidget(self.comboBoxType, alignment=Qt.AlignTop)

        vbox2 = QVBoxLayout()
        self.labelWebsite = QLabel(self.window)
        self.labelWebsite.setText("Website :")
        self.labelWebsite.setFont(QtGui.QFont("Sanserif", 15))
        vbox2.addWidget(self.labelWebsite, alignment=Qt.AlignBottom)

        self.websiteValue = QLineEdit(self.window)
        self.websiteValue.setFont(QtGui.QFont("Sanserif", 15))
        self.websiteValue.textChanged.connect(self.checkAllValueWebsite)
        self.websiteValue.returnPressed.connect(self.savePassword)
        vbox2.addWidget(self.websiteValue, alignment=Qt.AlignTop)

        vbox3 = QVBoxLayout()
        vbox3.setStretch(1, 1)
        self.labelUsername = QLabel(self.window)
        self.labelUsername.setText("Username :")
        self.labelUsername.setFont(QtGui.QFont("Sanserif", 15))
        vbox3.addWidget(self.labelUsername, alignment=Qt.AlignBottom)

        self.usernameValue = QLineEdit(self.window)
        self.usernameValue.setFont(QtGui.QFont("Sanserif", 15))
        self.usernameValue.textChanged.connect(self.checkAllValueWebsite)
        self.usernameValue.returnPressed.connect(self.savePassword)
        vbox3.addWidget(self.usernameValue, alignment=Qt.AlignTop)

        vbox4 = QVBoxLayout()
        vbox4.setStretch(1, 1)
        self.labelPassword = QLabel(self.window)
        self.labelPassword.setText("Suggested Password :")
        self.labelPassword.setFont(QtGui.QFont("Sanserif", 15))
        vbox4.addWidget(self.labelPassword, alignment=Qt.AlignBottom)

        self.passwordValue = QLineEdit(self.window)
        self.passwordValue.setText(self.get_random_password(32))
        self.passwordValue.setFont(QtGui.QFont("Sanserif", 15))
        self.passwordValue.returnPressed.connect(self.savePassword)
        self.passwordValue.textChanged.connect(self.checkAllValueWebsite)
        vbox4.addWidget(self.passwordValue, alignment=Qt.AlignTop)

        self.buttonValidate = QPushButton(self.window)
        self.buttonValidate.setText("Create the password")
        self.buttonValidate.setFont(QtGui.QFont("Sanserif", 15))
        self.buttonValidate.setFixedHeight(50)
        self.buttonValidate.setFixedWidth(230)
        self.buttonValidate.setEnabled(False)
        self.buttonValidate.clicked.connect(self.savePassword)

        gridLayout.addLayout(vbox1, 2, 0)
        gridLayout.addLayout(vbox2, 3, 0)
        gridLayout.addLayout(vbox3, 4, 0)
        gridLayout.addLayout(vbox4, 5, 0)
        gridLayout.addWidget(self.buttonValidate, 6, 0, alignment=Qt.AlignCenter)
        groupBox.setMaximumHeight(400)
        groupBox.setLayout(gridLayout)
        return groupBox

    def createCreditCardsForm(self):
        groupBox = QGroupBox()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.labelNew = QLabel(self.window)
        self.labelNew.setText("Create new Credit Cards")
        self.labelNew.setFont(QtGui.QFont("Sanserif", 25))
        self.labelNew.setAlignment(Qt.AlignHCenter)
        gridLayout.addWidget(self.labelNew)

        vbox1 = QVBoxLayout()
        self.comboBoxType = QComboBox(self.window)
        self.comboBoxType.setFont(QtGui.QFont("Sanserif", 15))
        self.comboBoxType.addItem("Credit Cards")
        self.comboBoxType.addItem("Website")
        self.comboBoxType.currentTextChanged.connect(self.changedTextType)
        vbox1.addWidget(self.comboBoxType, alignment=Qt.AlignTop)

        vbox2 = QVBoxLayout()
        self.labelBank = QLabel(self.window)
        self.labelBank.setText("Bank Name :")
        self.labelBank.setFont(QtGui.QFont("Sanserif", 15))
        vbox2.addWidget(self.labelBank, alignment=Qt.AlignBottom)

        self.bankValue = QLineEdit(self.window)
        self.bankValue.setFont(QtGui.QFont("Sanserif", 15))
        self.bankValue.textChanged.connect(self.checkAllValueCards)
        self.bankValue.returnPressed.connect(self.saveCreditCards)
        vbox2.addWidget(self.bankValue, alignment=Qt.AlignTop)

        vbox3 = QVBoxLayout()
        vbox3.setStretch(1, 1)
        self.labelNumber = QLabel(self.window)
        self.labelNumber.setText("Cards Number :")
        self.labelNumber.setFont(QtGui.QFont("Sanserif", 15))
        vbox3.addWidget(self.labelNumber, alignment=Qt.AlignBottom)

        self.numberValue = QLineEdit(self.window)
        self.numberValue.setFont(QtGui.QFont("Sanserif", 15))
        self.numberValue.textChanged.connect(self.checkAllValueCards)
        self.numberValue.returnPressed.connect(self.saveCreditCards)
        vbox3.addWidget(self.numberValue, alignment=Qt.AlignTop)

        vbox4 = QVBoxLayout()
        vbox4.setStretch(1, 1)
        self.labelDateCode = QLabel(self.window)
        self.labelDateCode.setText("Date and Code :")
        self.labelDateCode.setFont(QtGui.QFont("Sanserif", 15))
        vbox4.addWidget(self.labelDateCode, alignment=Qt.AlignBottom)

        self.dateCodeValue = QLineEdit(self.window)
        self.dateCodeValue.setFont(QtGui.QFont("Sanserif", 15))
        self.dateCodeValue.returnPressed.connect(self.saveCreditCards)
        self.dateCodeValue.textChanged.connect(self.checkAllValueCards)
        vbox4.addWidget(self.dateCodeValue, alignment=Qt.AlignTop)

        self.buttonValidate = QPushButton(self.window)
        self.buttonValidate.setText("Create the credit cards")
        self.buttonValidate.setFont(QtGui.QFont("Sanserif", 15))
        self.buttonValidate.setFixedHeight(50)
        self.buttonValidate.setFixedWidth(240)
        self.buttonValidate.setEnabled(False)
        self.buttonValidate.clicked.connect(self.saveCreditCards)

        gridLayout.addLayout(vbox1, 2, 0)
        gridLayout.addLayout(vbox2, 3, 0)
        gridLayout.addLayout(vbox3, 4, 0)
        gridLayout.addLayout(vbox4, 5, 0)
        gridLayout.addWidget(self.buttonValidate, 6, 0, alignment=Qt.AlignCenter)
        groupBox.setMaximumHeight(400)
        groupBox.setLayout(gridLayout)
        return groupBox



    def savePassword(self):
        if len(self.websiteValue.text()) > 0 and len(self.usernameValue.text()) > 0 and len(self.passwordValue.text()) > 0:
            self.buttonValidate.setEnabled(True)
            password = "Website=!=" + str(self.websiteValue.text()) + "!?&User=!=" + str(self.usernameValue.text()) \
                       + "!?&Password=!=" + str(self.passwordValue.text())
            self.window.goToPasswordScreen(password=password, cryptFile=None, user=None)
        else:
            self.buttonValidate.setEnabled(False)

    def checkAllValueWebsite(self):
        if len(self.websiteValue.text()) > 0 and len(self.usernameValue.text()) > 0 and len(self.passwordValue.text()) > 0:
            self.buttonValidate.setEnabled(True)
        else:
            self.buttonValidate.setEnabled(False)

    def checkAllValueCards(self):
        if len(self.bankValue.text()) > 0 and len(self.numberValue.text()) > 0 and len(self.dateCodeValue.text()) > 0:
            self.buttonValidate.setEnabled(True)
        else:
            self.buttonValidate.setEnabled(False)

    def saveCreditCards(self):
        if len(self.bankValue.text()) > 0 and len(self.numberValue.text()) > 0 and len(self.dateCodeValue.text()) > 0:
            self.buttonValidate.setEnabled(True)
            password = "Bank=!=" + str(self.bankValue.text()) + "!?&Number=!=" + str(self.numberValue.text()) \
                       + "!?&DateCode=!=" + str(self.dateCodeValue.text())
            self.window.goToPasswordScreen(password=password, cryptFile=None, user=None)
        else:
            self.buttonValidate.setEnabled(False)

    def get_random_password(self, size):
        source = string.ascii_letters + string.digits
        return ''.join((random.choice(source) for i in range(size)))

    def changedTextType(self):
        if self.textType != str(self.comboBoxType.currentText()):
            self.textType = self.comboBoxType.currentText()
            if str(self.comboBoxType.currentText()) == "Website":
                self.removeWidget(self.groupBoxWaou)
                self.groupBoxWaou.deleteLater()
                self.groupBoxWaou = self.createPasswordForm()
                self.addWidget(self.groupBoxWaou)
            elif str(self.comboBoxType.currentText()) == "Credit Cards":
                self.removeWidget(self.groupBoxWaou)
                self.groupBoxWaou.deleteLater()
                self.groupBoxWaou = self.createCreditCardsForm()
                self.addWidget(self.groupBoxWaou)