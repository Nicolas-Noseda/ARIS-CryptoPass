from PyQt5 import QtGui
from PyQt5.QtCore import Qt
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

        self.labelBank = QLabel(self.window)
        self.labelBank.setText("Bank Name: ")
        self.labelBank.setFont(QtGui.QFont("Sanserif", 10))
        self.labelBank.setAlignment(Qt.AlignLeft)
        self.labelBank.setFixedWidth(100)
        gridLayout.addWidget(self.labelBank, 0, 0)

        self.labelNumber = QLabel(self.window)
        self.labelNumber.setText("Cards Number: ")
        self.labelNumber.setFont(QtGui.QFont("Sanserif", 10))
        self.labelNumber.setAlignment(Qt.AlignLeft)
        self.labelNumber.setFixedWidth(100)
        gridLayout.addWidget(self.labelNumber, 1, 0)

        self.labelDateCode = QLabel(self.window)
        self.labelDateCode.setText("Date and Code: ")
        self.labelDateCode.setFont(QtGui.QFont("Sanserif", 10))
        self.labelDateCode.setAlignment(Qt.AlignLeft)
        self.labelDateCode.setFixedWidth(100)
        gridLayout.addWidget(self.labelDateCode, 2, 0)

        self.labelBankValue = QLabel(self.window)
        self.labelBankValue.setText(self.credit_cards.bank)
        self.labelBankValue.setFont(QtGui.QFont("Sanserif", 10))
        self.labelBankValue.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelBankValue, 0, 1)

        self.labelCardsNumberValue = QLabel(self.window)
        self.labelCardsNumberValue.setText("*Click 'Show' to view*")
        self.labelCardsNumberValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.labelCardsNumberValue.setFont(QtGui.QFont("Sanserif", 10))
        self.labelCardsNumberValue.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelCardsNumberValue, 1, 1)

        self.labelDateCodeValue = QLabel(self.window)
        self.labelDateCodeValue.setText("*Click 'Show' to view*")
        self.labelDateCodeValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.labelDateCodeValue.setFont(QtGui.QFont("Sanserif", 10))
        self.labelDateCodeValue.setAlignment(Qt.AlignLeft)
        gridLayout.addWidget(self.labelDateCodeValue, 2, 1)

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
            self.labelDateCodeValue.setText("*Click 'Show' to view*")
            self.buttonEyes.setText("Show")
        else:
            self.showCreditCards = True
            self.labelCardsNumberValue.setText(self.credit_cards.number)
            self.labelDateCodeValue.setText(self.credit_cards.dateCode)
            self.buttonEyes.setText("Hide")

    def deletePassword(self):
        self.window.deletePasswordFromPasswordList(self.credit_cards_string)