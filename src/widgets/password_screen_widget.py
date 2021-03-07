from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QInputMethodEvent
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QScrollArea, QScrollBar, QPushButton, QHBoxLayout, \
    QLineEdit, QLabel

from src.widgets.password.credit_cards_widget import CreditCardsWidget
from src.widgets.password.website_password_widget import WebsitePasswordWidget


class PasswordScreenWidget(QVBoxLayout):
    def __init__(self, *args, window, passwordList, cryptFile):
        super().__init__(*args)
        self.window = window
        self.cryptFile = cryptFile
        self.passwordListFull = passwordList
        self.passwordList = passwordList
        self.createWidget()
        self.addWidget(self.screenBox)

    def createWidget(self):
        self.screenBox = QGroupBox()
        self.gridLayout = QGridLayout()
        self.screenBox.setStyleSheet("QGroupBox{border:none}")


        searchBox = QGroupBox()
        searchBox.setStyleSheet("QGroupBox{border:none}")

        hboxSearch = QHBoxLayout()

        self.lineEditSearch = QLineEdit()
        self.lineEditSearch.setFont(QtGui.QFont("Sanserif", 15))
        self.lineEditSearch.setPlaceholderText("Type to search")
        self.lineEditSearch.textEdited.connect(self.changeAllPassword)
        hboxSearch.addWidget(self.lineEditSearch)
        searchBox.setLayout(hboxSearch)

        self.gridLayout.addWidget(searchBox, 0, 0)

        self.scrollArea = self.createScrollArea()

        buttonCreateNewPassword = QPushButton(self.window)
        buttonCreateNewPassword.setText("Create new password")
        buttonCreateNewPassword.setFixedHeight(25)
        buttonCreateNewPassword.setFixedWidth(150)
        buttonCreateNewPassword.clicked.connect(self.createNewPassword)
        self.gridLayout.addWidget(self.scrollArea, 1, 0)
        self.gridLayout.addWidget(buttonCreateNewPassword, 2, 0, alignment=Qt.AlignCenter)
        self.screenBox.setLayout(self.gridLayout)

    def createNewPassword(self):
        self.window.goToCreateNewPassword()

    def changeAllPassword(self):
        passwordList = ""
        if self.passwordList != "":
            password_split = self.passwordList.split(";!&?;")
            if str(self.lineEditSearch.text()) != "":
                for password in password_split:
                    website = password.split("!?&")[0].split("=!=")[1]
                    user = password.split("!?&")[1].split("=!=")[1]
                    if str(self.lineEditSearch.text()).lower() in website.lower() or str(self.lineEditSearch.text()).lower() in user.lower():
                        if passwordList == "":
                            passwordList = password
                        else:
                            passwordList += ";!&?;" + password
                if passwordList != "":
                    self.passwordList = passwordList
            else:
                self.passwordList = self.passwordListFull
            self.gridLayout.removeWidget(self.scrollArea)
            self.scrollArea = self.createScrollArea()
            self.gridLayout.addWidget(self.scrollArea, 1, 0)

    def createScrollArea(self):
        scrollArea = QScrollArea()
        vboxPassword = QVBoxLayout()
        groupBoxPassword = QGroupBox()
        groupBoxPassword.setStyleSheet("QGroupBox{border:none}")
        if self.passwordList != "":
            password_split = self.passwordList.split(";!&?;")
            for password in password_split:
                if "Website" in password:
                    vboxPassword.addWidget(WebsitePasswordWidget(window=self.window, website_password=password),
                                           alignment=Qt.AlignTop)
                elif "Bank" in password:
                    vboxPassword.addWidget(CreditCardsWidget(window=self.window, credit_cards=password),
                                           alignment=Qt.AlignTop)
        else:
            labelNoPasswordSaved = QLabel(self.window)
            labelNoPasswordSaved.setText('You don\'t have saved password, click "Create new password" to save one')
            labelNoPasswordSaved.setWordWrap(True)
            vboxPassword.addWidget(labelNoPasswordSaved, alignment=Qt.AlignCenter)

        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setWidgetResizable(True)
        scrollArea.setFixedHeight(370)
        groupBoxPassword.setLayout(vboxPassword)
        scrollArea.setWidget(groupBoxPassword)
        return scrollArea
