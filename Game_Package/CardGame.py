from Game_Package.Card import Card
from Game_Package.DeckOfCards import DeckOfCards
from Game_Package.Player import Player
from string import capwords

class CardGame:
    def __init__(self, name1: str, name2: str, hand_size: int)-> None:
        """creates the class fields and calls new_game which shuffles the deck and sets the players hands"""
        name1 = self.verify_and_adjust_player_name(name1)
        name2 = self.verify_and_adjust_player_name(name2)
        hand_size = self.verify_and_adjust_hand_size(hand_size)
        if name1 == name2:
            raise ValueError("player names are the same")
        self.deck = DeckOfCards()
        self.player1 = Player(name1, hand_size)
        self.player2 = Player(name2, hand_size)
        self.new_game()

    def new_game(self)-> None:
        """if the game hasn't started, shuffles the deck and sets the players hands, else prints an error"""
        if len(self.deck.card_list) == 52:
            self.deck.cards_shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)
        else:
            print("Error - method called from outside __init__")

    def get_winner(self)-> Player or None:
        """returns the player with more cards in their deck. if the amount is equal, returns None"""
        player1_cards = len(self.player1.player_deck)
        player2_cards = len(self.player2.player_deck)
        if player1_cards > player2_cards:
            return self.player1
        if player1_cards < player2_cards:
            return self.player2
        return None

    @staticmethod
    def verify_and_adjust_player_name(name: str) -> str:
        if type(name) is not str:
            raise TypeError("name type is not str")
        if len(name) == 0:
            raise ValueError("name is empty")
        return capwords(name)

    @staticmethod
    def verify_and_adjust_hand_size(size: int) -> int:
        if type(size) is not int:
            raise TypeError("hand size type is not int")
        if not 10 <= size <= 26:
            return 26
        else:
            return size