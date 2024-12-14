from Game_Package.Card import Card
from Game_Package.DeckOfCards import DeckOfCards
from Game_Package.Player import Player

class CardGame:
    def __init__(self, names, hand_size):
        self.deck = None
        self.players = None
        self.new_game(names, hand_size)

    def new_game(self, names, hand_size):
        if self.deck is not None and self.players is not None:
            deck = DeckOfCards()
            deck.cards_shuffle()
            self.deck = deck
            self.players = []
            for i in range(len(names)):
                self.players.append(Player(names[i], hand_size))
                for j in range(hand_size):
                    self.players[i].add_card(deck.deal_one())

    def get_winner(self):
        card_amounts = self.players_card_amount()
        maximum_cards = max(card_amounts)
        if card_amounts.count(maximum_cards) > 1:
            return None
        winner_index = card_amounts.index(maximum_cards)
        return self.players[winner_index]

    def players_card_amount(self):
        """returns a list with the player card amounts at the same indices of the correlated list of players"""
        card_amounts = []
        for i in self.players:
            card_amounts.append(len(i.player_deck))
        return card_amounts

    @staticmethod
    def verify_names(names):
        if type(names) is not list:
            raise TypeError
        for name in names:
            if type(name) is not str:
                raise TypeError
            if not len(name) > 0:
                raise ValueError

    @staticmethod
    def replace_invalid_names_with_bob(names):
        bob_number = 1
        for index in range(len(names)):
            if type(names[index]) is not str:
                names[index] = f"bob{bob_number}"
                bob_number += 1

    @staticmethod
    def verify_card_player_number(self, players, hand_size):
        if players * hand_size > 52:
            raise ValueError