from Game_Package.Card import Card
from Game_Package.DeckOfCards import DeckOfCards
from Game_Package.Player import Player

# 2 players ONLY
class CardGame:
    def __init__(self, name1, name2, hand_size):
        self.deck = None
        self.player1 = None
        self.player2 = None
        self.new_game(name1, name2, hand_size)

    def new_game(self, name1, name2, hand_size):
        if self.deck is not None and self.player1 is not None and self.player2 is not None:
            self.deck = DeckOfCards()
            self.deck.cards_shuffle()
            self.player1 = Player(name1, hand_size)
            self.player2 = Player(name2, hand_size)
        print("Error - method called from outside __init__")

    def get_winner(self):
        player1_cards = len(self.player1.player_deck)
        player2_cards = len(self.player2.player_deck)
        if player1_cards > player2_cards:
            return self.player1
        if player1_cards < player2_cards:
            return self.player2
        return None

    @staticmethod
    def replace_invalid_names_with_bob(names):
        bob_number = 1
        for index in range(len(names)):
            if type(names[index]) is not str:
                names[index] = f"bob{bob_number}"
                bob_number += 1

    @staticmethod
    def verify_card_player_number(players, hand_size):
        if players * hand_size > 52:
            raise ValueError