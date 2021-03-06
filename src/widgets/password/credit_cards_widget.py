from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGroupBox, QGridLayout, QLabel, QPushButton

from src.model.credit_cards_model import CreditCardsModel


class CreditCardsWidget(QWidget):

    showCreditCards = False

    def __init__(self, *args, window, credit_cards):
        super().__init__(*args)
        self.credit_cards_string = credit_cards
        self.window = window
        self.credit_cards = CreditCardsModel(credit_cards)
        self.createWidget()

    def createWidget(self):
        self.groupBox = QGroupBox()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(3)

        self.labelNumber = QLabel(self.window)
        self.labelNumber.setText("Cards Number: ")
        self.labelNumber.setFont(QtGui.QFont("Sanserif", 10))
        self.labelNumber.setAlignment(Qt.AlignLeft)
        self.labelNumber.setFixedWidth(100)
        gridLayout.addWidget(self.labelNumber, 0, 0)

        self.labelDate = QLabel(self.window)
        self.labelDate.setText("Date: ")
        self.labelDate.setFont(QtGui.QFont("Sanserif", 10))
        self.labelDate.setAlignment(Qt.AlignLeft)
        self.labelDate.setFixedWidth(100)
        gridLayout.addWidget(self.labelDate, 1, 0)

        self.labelCode = QLabel(self.window)
        self.labelCode.setText("Code: ")
        self.labelCode.setFont(QtGui.QFont("Sanserif", 10))
        self.labelCode.setAlignment(Qt.AlignLeft)
        self.labelCode.setFixedWidth(100)
        gridLayout.addWidget(self.labelCode, 2, 0)

        self.labelCardsNumberValue = QLabel(self.window)
        self.labelCardsNumberValue.setText("*Click 'Show' to view*")
        self.labelCardsNumberValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.labelCardsNumberValue.setFont(QtGui.QFont("Sanserif", 10))
        self.labelCardsNumberValue.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelCardsNumberValue, 0, 1)

        self.labelDateValue = QLabel(self.window)
        self.labelDateValue.setText("*Click 'Show' to view*")
        self.labelDateValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.labelDateValue.setFont(QtGui.QFont("Sanserif", 10))
        self.labelDateValue.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelDateValue, 1, 1)

        self.labelCodeValue = QLabel(self.window)
        self.labelCodeValue.setText("*Click 'Show' to view*")
        self.labelCodeValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.labelCodeValue.setFont(QtGui.QFont("Sanserif", 10))
        self.labelCodeValue.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelCodeValue, 2, 1)

        self.buttonEyes = QPushButton(self.window)
        self.buttonEyes.setText("Show")
        self.buttonEyes.setFont(QtGui.QFont("Sanserif", 10))
        self.buttonEyes.clicked.connect(self.buttonEyesClicked)
        self.buttonEyes.setFixedWidth(80)
        gridLayout.addWidget(self.buttonEyes, 1, 2)

        self.buttonDelete = QPushButton(self.window)
        self.buttonDelete.setText("X")
        self.buttonDelete.setFont(QtGui.QFont("Sanserif", 10))
        self.buttonDelete.setFixedWidth(20)
        self.buttonDelete.clicked.connect(self.deletePassword)
        gridLayout.addWidget(self.buttonDelete, 0, 2, alignment=Qt.AlignRight)

        self.setFixedHeight(100)
        self.setLayout(gridLayout)

    def buttonEyesClicked(self):
        if self.showCreditCards:
            self.showCreditCards = False
            self.labelCardsNumberValue.setText("*Click 'Show' to view*")
            self.labelDateValue.setText("*Click 'Show' to view*")
            self.labelCodeValue.setText("*Click 'Show' to view*")
            self.buttonEyes.setText("Show")
        else:
            self.showCreditCards = True
            self.labelCardsNumberValue.setText(self.credit_cards.number)
            self.labelDateValue.setText(self.credit_cards.date)
            self.labelCodeValue.setText(self.credit_cards.code)
            self.buttonEyes.setText("Hide")

    def deletePassword(self):
        self.window.deletePasswordFromPasswordList(self.credit_cards_string)