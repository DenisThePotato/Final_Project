from unittest import TestCase
from Game_Package.DeckOfCards import DeckOfCards

class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    #add init check


    def test_cards_shuffle(self):
        """this test will fail with a chance of (1/52)**len(card_list)"""
        deck = DeckOfCards()
        deck.cards_shuffle()
        self.assertNotEqual(deck, self.deck.card_list)

    def test_deal_one_valid(self):
        card = self.deck.deal_one()
        self.assertNotIn(card, self.deck.card_list)

    def test_deal_one_invalid_empty_list(self):
        self.deck.card_list = []
        self.assertEqual(type(None), type(self.deck.deal_one()))


