from unittest import TestCase
from unittest import mock
from Game_Package.Player import Player
from Game_Package.Card import Card
from Game_Package.DeckOfCards import DeckOfCards

class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("bob", 20)
        self.player.player_deck.append(Card(2, 2))

    def test_init_valid_hand_size_high(self):
        player = Player("bob", 26)
        self.assertEqual(26, player.hand_size)

    def test_init_valid_hand_size_low(self):
        player = Player("bob", 10)
        self.assertEqual(10, player.hand_size)

    def test_init_invalid_hand_size_high(self):
        player = Player("bob", 27)
        self.assertEqual(26, player.hand_size)

    def test_init_invalid_hand_size_low(self):
        player = Player("bob", 9)
        self.assertEqual(26, player.hand_size)

    def test_init_invalid_player_name_type(self):
        with self.assertRaises(TypeError):
            Player(5, 20)

    def test_init_invalid_player_name_length(self):
        with self.assertRaises(ValueError):
            Player("", 20)

    @mock.patch('Game_Package.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, 1))
    def test_set_hand(self, mock_deal_one):
        player = Player("bob", 20)
        player.set_hand(DeckOfCards())
        self.assertEqual(20, len(player.player_deck))
        self.assertIn(Card(1, 1), player.player_deck)
        self.assertEqual(20, mock_deal_one.call_count)

    def test_get_card(self):
        card = self.player.get_card()
        self.assertNotIn(card, self.player.player_deck)
        self.assertEqual(type(card), Card)

    def test_get_card_empty_list(self):
        self.player.player_deck = []
        self.assertEqual(type(None), type(self.player.get_card()))

    def test_add_card_valid(self):
        self.player.player_deck = []
        self.player.add_card(Card(1, 1))
        self.assertIn(Card(1, 1), self.player.player_deck)

    def test_card_invalid_type(self):
        with self.assertRaises(TypeError):
            self.player.add_card(4)
