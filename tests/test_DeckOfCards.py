from unittest import TestCase
from Game_Package.DeckOfCards import DeckOfCards

class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def tearDown(self):
        pass

    def test_cards_shuffle(self):
        """this test will fail with a chance of (1/52)**len(card_list)"""
        deck = []
        for i in range(len(self.deck.card_list)):
            deck.append(self.deck.card_list[i])
        self.assertNotEqual(deck, self.deck)

    def test_deal_one_valid(self):
        card = self.deck.deal_one()
        self.assertNotIn(card, self.deck.card_list)

    def test_deal_one_invalid_empty_list(self):
        for i in range(52):
            self.deck.deal_one()
        # the better option would probably be self.deck.card_list = []
        # then there would be no dependency on deal_one.
        self.assertEqual(type(None), type(self.deck.deal_one()))


