from Game_Package.Card import Card
from random import shuffle
from random import randint

class DeckOfCards:
    def __init__(self):
        self.card_list = []
        for i in range(4):
            for j in range(13):
                self.card_list.append(Card(i + 1, j + 1))

    def cards_shuffle(self)-> None:
        """organizes the card list in random order"""
        if self.verify_deck_not_empty():
            shuffle(self.card_list)

    def deal_one(self)-> Card or None:
        """removes one card from the card list and returns it"""
        if self.verify_deck_not_empty():
            return self.card_list.pop(randint(0, len(self.card_list) - 1))

    def verify_deck_not_empty(self):
        """verifies that the card list is not empty"""
        if len(self.card_list) > 0:
            return True
        return False

    def verify_deck_validity(self):
        """verifies that all objects in the card list are cards"""
        for card in self.card_list:
            if type(card) is not Card:
                raise TypeError