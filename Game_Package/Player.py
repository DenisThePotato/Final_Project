from string import capwords
from Game_Package.DeckOfCards import DeckOfCards
from random import randint
from Game_Package.Card import Card

class Player:
    def __init__(self, player_name: str, hand_size = 26)-> None:
        self.player_name = self.verify_and_adjust_player_name(player_name)
        self.hand_size = self.verify_and_adjust_hand_size(hand_size)
        self.player_deck = []

    def __str__(self)-> str:
        return f"{self.player_name}"

    def set_hand(self, card_deck: DeckOfCards)-> None:
        """fills the players deck with required amount of cards"""
        if self.verify_deck(card_deck):
            for i in range(self.hand_size):
                self.player_deck.append(card_deck.deal_one())

    def get_card(self)-> Card or None:
        """deletes a card from the players deck and returns it"""
        if len(self.player_deck) > 0:
            return self.player_deck.pop(randint(0, len(self.player_deck) - 1))

    def add_card(self, card: Card)-> None:
        """validates the card and then adds it to the players deck"""
        if type(card) is not Card:
            raise TypeError
        self.player_deck.append(card)

    @staticmethod
    def verify_and_adjust_player_name(name: str)-> str:
        if type(name) is not str:
            raise TypeError("name type is not str")
        if len(name) == 0:
            raise ValueError("name is empty")
        return capwords(name)

    @staticmethod
    def verify_and_adjust_hand_size(size: int)-> int:
        if type(size) is not int:
            raise TypeError("hand size type is not int")
        if not 10 <= size <= 26:
            return 26
        else:
            return size

    def verify_deck(self, deck: DeckOfCards)-> bool:
        if type(deck) is not DeckOfCards:
            raise TypeError("object type is not DeckOfCards")
        if len(deck.card_list) < self.hand_size:
            return False
        return True