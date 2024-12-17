from Game_Package.Card import Card
from random import shuffle
from random import randint

class DeckOfCards:
    """initializes a deck with 52 unique cards"""
    def __init__(self)-> None:
        self.card_list = []
        for i in range(4):
            for j in range(13):
                self.card_list.append(Card(i + 1, j + 1))

    def cards_shuffle(self)-> None:
        """organizes the card list in random order"""
        shuffle(self.card_list)

    def deal_one(self)-> Card or None:
        """removes one card from the card list and returns it"""
        if len(self.card_list) > 0:
            return self.card_list.pop(randint(0, len(self.card_list) - 1))