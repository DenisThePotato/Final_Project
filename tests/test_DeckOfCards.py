from unittest import TestCase
from Game_Package.DeckOfCards import DeckOfCards
from Game_Package.Card import Card

class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_init_valid_deck_length(self):
        self.assertEqual(52, len(self.deck.card_list))

    def test_init_valid_card_uniqueness(self):
        for i in range(52):
            self.assertEqual(1, self.deck.card_list.count(self.deck.card_list[i]))

    def test_init_valid_deck_card_existence(self):
        expected_deck = []
        for i in range(4):
            for j in range(13):
                expected_deck.append(Card(i + 1, j + 1))
        for i in range(52):
            self.assertEqual(expected_deck[i], self.deck.card_list[i])

    def test_cards_shuffle(self):
        """this test will fail with a chance of (1/52)**len(card_list)"""
        deck = DeckOfCards()
        deck.cards_shuffle()
        self.assertNotEqual(deck, self.deck.card_list)

    def test_deal_one_valid(self):
        card = self.deck.deal_one()
        card_index = card.value + (card.suit - 1) * 13
        self.assertNotEqual(card, self.deck.card_list[card_index])
        self.assertEqual(Card, type(card))
        self.assertNotIn(card, self.deck.card_list)

    def test_deal_one_invalid_empty_list(self):
        self.deck.card_list = []
        self.assertEqual(type(None), type(self.deck.deal_one()))


