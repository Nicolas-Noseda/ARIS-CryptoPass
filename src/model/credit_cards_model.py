class CreditCardsModel:

    number = ""
    date = ""
    code = ""

    def __init__(self, credit_cards):
        credit_cards_split = credit_cards.split("!?&")
        self.number = credit_cards_split[0].split("=!=")[1]
        self.date = credit_cards_split[1].split("=!=")[1]
        self.code = credit_cards_split[2].split("=!=")[1]