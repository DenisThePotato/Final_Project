from Game_Package.Card import Card

class DeckOfCards:
    def __init__(self):
        self.card_list = []
        for i in range(4):
            for j in range(13):
                self.card_list.append(Card(i + 1, j + 1))