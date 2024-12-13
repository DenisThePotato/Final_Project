from string import capwords
from Game_Package.DeckOfCards import DeckOfCards
from random import randint
from Game_Package.Card import Card

class Player:
    def __init__(self, player_name, hand_size):
        self.player_name = self.verify_player_name(player_name)
        self.hand_size = self.verify_hand_size(hand_size)
        self.player_deck = []

    def set_hand(self, card_deck : DeckOfCards):
        self.hand_size = self.verify_hand_size(self.hand_size)
        for i in range(self.hand_size):
            self.player_deck.append(card_deck.deal_one())

    def get_card(self):
        if self.verify_deck_not_empty():
            return self.player_deck.pop(randint(0, len(self.player_deck) - 1))

    def add_card(self, card : Card):
        """validates the card and then adds it to the players deck"""
        Card.verify_card_validity(card)
        self.player_deck.append(card)

    @staticmethod
    def verify_player_name(name)-> str:
        if type(name) is not str:
            raise TypeError
        if len(name) == 0:
            raise ValueError
        return capwords(name)

    @staticmethod
    def verify_hand_size(size):
        if type(size) is not int:
            raise TypeError
        if not 10 <= size <= 26:
            return 26
        else:
            return size

    def verify_deck_not_empty(self):
        """verifies that the card list is not empty"""
        if len(self.player_deck) > 0:
            return True
        return False
