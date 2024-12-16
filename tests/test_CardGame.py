from unittest import TestCase
from Game_Package.CardGame import CardGame
from Game_Package.Player import Player

class TestCardGame(TestCase):
    def setUp(self):
        self.card_game = CardGame("bob", "bobby", 20)

    def tearDown(self):
        pass

    def test_init_valid(self):
        card_game = CardGame("bob", "bobby", 20)
        self.assertEqual(Player("bob", 20), self.card_game.player1)
        self.assertEqual(Player("bobby", 20), self.card_game.player2)
        self.assertEqual(20, card_game.hand_size)

    def test_init_invalid_name(self):
        with self.assertRaises(TypeError):
            CardGame(123, "bob", 20)
        with self.assertRaises(TypeError):
            CardGame("bob", 123, 20)

    def test_init_invalid_hand_size(self):
        with self.assertRaises(TypeError):
            CardGame("bobby", "bob", "20")

    def test_new_game_invalid_not_init(self):
        self.assertEqual(type(None), type(self.card_game.new_game("bob", "bobby", 20)))

    def test_get_winner_valid(self):
        self.card_game.player1.get_card()
        self.assertEqual(self.card_game.player2, self.card_game.get_winner())

    def test_get_winner_valid_tie(self):
        self.assertEqual(None, self.card_game.get_winner())
        pass





