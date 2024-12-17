from Game_Package.Card import Card
from Game_Package.DeckOfCards import DeckOfCards
from Game_Package.Player import Player

class CardGame:
    def __init__(self, name1: str, name2: str, hand_size: int)-> None:
        if name1 == name2:
            raise ValueError("player names are the same")
        self.deck = None
        self.player1 = None
        self.player2 = None
        self.new_game(name1, name2, hand_size)

    def new_game(self, name1: str, name2: str, hand_size: int)-> None:
        if self.deck is None:
            self.deck = DeckOfCards()
            self.deck.cards_shuffle()
            self.player1 = Player(name1, hand_size)
            self.player2 = Player(name2, hand_size)
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)
        else:
            print("Error - method called from outside __init__")

    def get_winner(self)-> Player or None:
        player1_cards = len(self.player1.player_deck)
        player2_cards = len(self.player2.player_deck)
        if player1_cards > player2_cards:
            return self.player1
        if player1_cards < player2_cards:
            return self.player2
        return None