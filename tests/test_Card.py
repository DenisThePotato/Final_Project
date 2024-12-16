from unittest import TestCase
from Game_Package.Card import Card

class TestCard(TestCase):
    def setUp(self):
        self.high_card = Card(4, 13)
        self.low_card = Card(1, 1)

    def test_init_valid_high(self):
        self.assertEqual(4, self.high_card.suit)
        self.assertEqual(13, self.high_card.value)

    def test_init_valid_low(self):
        self.assertEqual(1, self.low_card.suit)
        self.assertEqual(1, self.low_card.value)

    def test_init_invalid_suit_type(self):
        with self.assertRaises(TypeError):
            Card("5", 7)

    def test_init_invalid_suit_high(self):
        with self.assertRaises(ValueError):
            Card(5, 7)

    def test_init_invalid_suit_low(self):
        with self.assertRaises(ValueError):
            Card(0, 7)

    def test_init_invalid_value_type(self):
        with self.assertRaises(TypeError):
            Card(2, "7")

    def test_init_invalid_value_high(self):
        with self.assertRaises(ValueError):
            Card(2, 14)

    def test_init_invalid_value_low(self):
        with self.assertRaises(ValueError):
            Card(2, 0)

    def test_str(self):
        self.high_card.suit = 1
        high_card_as_string = str(self.high_card)
        self.assertEqual("Ace of Diamonds", high_card_as_string)

    def test_gt_valid_greater_value(self):
        self.assertTrue(self.high_card > self.low_card)

    def test_gt_valid_greater_suit(self):
        self.low_card.value = 13
        self.assertTrue(self.high_card > self.low_card)

    def test_gt_valid_equal(self):
        self.assertFalse(self.high_card > self.high_card)

    def test_gt_valid_lower(self):
        self.assertFalse(self.low_card > self.high_card)

    def test_gt_invalid_type(self):
        with self.assertRaises(TypeError):
            self.high_card > 4

    def test_eq_valid_not_equal(self):
        self.assertFalse(self.high_card == self.low_card)

    def test_eq_valid_equal(self):
        card = Card(4, 13)
        self.assertTrue(self.high_card == card)

    def test_eq_invalid_type(self):
        with self.assertRaises(TypeError):
            self.high_card == 4
