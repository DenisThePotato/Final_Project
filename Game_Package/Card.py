# a class representing a  single card in a deck of 52 cards.
# each card has a suit from 1 to 4, and a value from 1 to 13.
class Card:

    def __init__(self, suit : int, value : int):
        """gets two int values and creates an object"""
        self.value = value
        self.suit = suit

    # NOT INCLUDED IN UNIT TESTS
    def __str__(self):
        return f"{self.value_to_str()} of {self.suit_to_str()}"

    # NOT INCLUDED IN UNIT TESTS
    def __repr__(self):
        pass

    def __gt__(self, other : 'Card'):
        """verifies the two cards for comparison, and compares them.
            raises exceptions when the objects are not valid"""
        self.verify_card_validity(self)
        self.verify_card_validity(other)
        if self.value == other.value:   # value is the same, suit is larger
            if self.suit > other.suit:
                return True
        if self.value > other.value:   # value is larger
            return True
        return False

    def __eq__(self, other : 'Card'):
        """verifies the two cards for comparison, and compares them.
                raises exceptions when the objects are not valid"""
        self.verify_card_validity(self)
        self.verify_card_validity(other)
        if self.value == other.value and self.suit == other.suit:
            return True
        return False

    def value_to_str(self):
        """returns the string associated with the value of the card"""
        match self.value:
            case 1:
                return "One"
            case 2:
                return "Two"
            case 3:
                return "Three"
            case 4:
                return "Four"
            case 5:
                return "Five"
            case 6:
                return "Six"
            case 7:
                return "Seven"
            case 8:
                return "Eight"
            case 9:
                return "Nine"
            case 10:
                return "Jack"
            case 11:
                return "Queen"
            case 12:
                return "King"
            case 13:
                return "Ace"

    def suit_to_str(self):
        """returns the string associated with the suit of the card"""
        match self.suit:
            case 1:
                return "Diamonds"
            case 2:
                return "Spades"
            case 3:
                return "Hearts"
            case 4:
                return "Clubs"

    @staticmethod
    def verify_value(value):
        """verifies the value of the object"""
        if type(value) is not int:
            raise TypeError
        if not 1 <= value <= 13:
            return ValueError

    @staticmethod
    def verify_suit(suit):
        """verifies the suit of the object"""
        if type(suit) is not int:
            raise TypeError
        if not 1 <= suit <= 4:
            return ValueError

    @staticmethod
    def verify_card_validity(card):
        """verify the cards validity"""
        if type(card) is not Card:
            raise TypeError
        Card.verify_value(card)
        Card.verify_suit(card)