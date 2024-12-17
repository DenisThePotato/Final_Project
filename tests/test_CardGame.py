from unittest import TestCase
from Game_Package.CardGame import CardGame
from Game_Package.DeckOfCards import DeckOfCards
from Game_Package.Player import Player

class TestCardGame(TestCase):
    def setUp(self):
        self.card_game = CardGame("bob", "bobby", 20)

    def test_init_valid(self):
        self.assertEqual("Bob", self.card_game.player1.player_name)
        self.assertEqual("Bobby", self.card_game.player2.player_name)
        self.assertEqual(20, len(self.card_game.player1.player_deck))
        self.assertEqual(20, len(self.card_game.player2.player_deck))
        self.assertTrue(self.card_game.deck is not None)
        self.assertEqual(12, len(self.card_game.deck.card_list))

    def test_init_invalid_name_type(self):
        with self.assertRaises(TypeError):
            CardGame(123, "bob", 20)
        with self.assertRaises(TypeError):
            CardGame("bob", 123, 20)

    def test_init_invalid_name_same(self):
        with self.assertRaises(ValueError):
            CardGame("bob", "bob", 20)

    def test_init_invalid_hand_size_type(self):
        with self.assertRaises(TypeError):
            CardGame("bobby", "bob", "20")

    def test_init_invalid_hand_size_low(self):
        card_game = CardGame("bobby", "bob", 9)
        self.assertEqual(26, len(card_game.player1.player_deck))

    def test_init_invalid_hand_size_high(self):
        card_game = CardGame("bobby", "bob", 27)
        self.assertEqual(26 ,len(card_game.player1.player_deck))

    def test_new_game_invalid_not_init(self):
        card_game = CardGame("bob", "bobby", 5)
        player1_clone = card_game.player1
        player2_clone = card_game.player2
        deck_clone = card_game.deck
        card_game.new_game()
        self.assertEqual(player1_clone.player_deck, card_game.player1.player_deck)
        self.assertEqual(player2_clone.player_deck, card_game.player2.player_deck)
        self.assertEqual(deck_clone, card_game.deck)

    def test_get_winner_valid(self):
        self.card_game.player1.get_card()
        self.assertEqual(self.card_game.player2, self.card_game.get_winner())

    def test_get_winner_valid_tie(self):
        self.assertEqual(None, self.card_game.get_winner())
        pass





