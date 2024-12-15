from string import capwords
from Game_Package.DeckOfCards import DeckOfCards
from random import randint
from Game_Package.Card import Card

class Player:
    def __init__(self, player_name, hand_size):
        self.player_name = self.verify_player_name(player_name)
        self.hand_size = self.verify_hand_size(hand_size)
        self.player_deck = []

    def __str__(self)-> str:
        return f"{self.player_name}"

    def set_hand(self, card_deck : DeckOfCards)-> None:
        """fills the players deck with required amount of cards"""
        self.hand_size = self.verify_hand_size(self.hand_size)
        for i in range(self.hand_size):
            self.player_deck.append(card_deck.deal_one())

    def get_card(self)-> Card:
        """deletes a card from the players deck and returns it"""
        if len(self.player_deck) > 0:
            return self.player_deck.pop(randint(0, len(self.player_deck) - 1))

    def add_card(self, card : Card)-> None:
        """validates the card and then adds it to the players deck"""
        if type(card) is not Card:
            raise TypeError
        self.player_deck.append(card)

    @staticmethod
    def verify_player_name(name: str)-> str:
        if type(name) is not str:
            raise TypeError
        if len(name) == 0:
            raise ValueError
        return capwords(name)

    @staticmethod
    def verify_hand_size(size: int)-> int:
        if type(size) is not int:
            raise TypeError
        if not 10 <= size <= 26:
            return 26
        else:
            return size