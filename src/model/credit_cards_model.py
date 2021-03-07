class CreditCardsModel:

    bank = ""
    number = ""
    dateCode = ""

    def __init__(self, credit_cards):
        credit_cards_split = credit_cards.split("!?&")
        self.bank = credit_cards_split[0].split("=!=")[1]
        self.number = credit_cards_split[1].split("=!=")[1]
        self.dateCode = credit_cards_split[2].split("=!=")[1]