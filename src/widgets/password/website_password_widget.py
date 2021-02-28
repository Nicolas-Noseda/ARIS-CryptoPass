from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QGroupBox, QLabel, QPushButton, QWidget

from src.model.website_password_model import WebsitePasswordModel


class WebsitePasswordWidget(QWidget):

    showPassword = False

    def __init__(self, *args, window, website_password):
        super().__init__(*args)
        self.window = window
        self.website_password = WebsitePasswordModel(website_password)
        self.createWidget()

    def createWidget(self):
        self.groupBox = QGroupBox()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(3)

        self.labelWebsite = QLabel(self.window)
        self.labelWebsite.setText("Website: ")
        self.labelWebsite.setFont(QtGui.QFont("Sanserif", 10))
        self.labelWebsite.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelWebsite, 0, 0)

        self.labelUser = QLabel(self.window)
        self.labelUser.setText("Username: ")
        self.labelUser.setFont(QtGui.QFont("Sanserif", 10))
        self.labelUser.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelUser, 1, 0)

        self.labelPassword = QLabel(self.window)
        self.labelPassword.setText("Password: ")
        self.labelPassword.setFont(QtGui.QFont("Sanserif", 10))
        self.labelPassword.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelPassword, 2, 0)

        self.labelWebsiteValue = QLabel(self.window)
        self.labelWebsiteValue.setText(self.website_password.website)
        self.labelWebsiteValue.setFont(QtGui.QFont("Sanserif", 10))
        self.labelWebsiteValue.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelWebsiteValue, 0, 1)

        self.labelUserValue = QLabel(self.window)
        self.labelUserValue.setText("****************")
        self.labelUserValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.labelUserValue.setFont(QtGui.QFont("Sanserif", 10))
        self.labelUserValue.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelUserValue, 1, 1)

        self.labelPasswordValue = QLabel(self.window)
        self.labelPasswordValue.setText("****************")
        self.labelPasswordValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.labelPasswordValue.setFont(QtGui.QFont("Sanserif", 10))
        self.labelPasswordValue.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelPasswordValue, 2, 1)

        self.buttonEyes = QPushButton(self.window)
        self.buttonEyes.setText("Show")
        self.buttonEyes.setFont(QtGui.QFont("Sanserif", 10))
        self.buttonEyes.clicked.connect(self.buttonEyesClicked)
        self.buttonEyes.setFixedWidth(80)
        gridLayout.addWidget(self.buttonEyes, 1, 2)

        self.setFixedHeight(100)
        self.setLayout(gridLayout)

    def buttonEyesClicked(self):
        if self.showPassword:
            self.showPassword = False
            self.labelPasswordValue.setText("****************")
            self.labelUserValue.setText("****************")
            self.buttonEyes.setText("Show")
        else:
            self.showPassword = True
            self.labelPasswordValue.setText(self.website_password.password)
            self.labelUserValue.setText(self.website_password.username)
            self.buttonEyes.setText("Hide")
