# a class representing a  single card in a deck of 52 cards.
# each card has a suit from 1 to 4, and a value from 1 to 13.
class Card:
    def __init__(self, suit: int, value: int)-> None:
        """gets two int values and creates an object"""
        self.verify_suit(suit)
        self.verify_value(value)
        self.value = value
        self.suit = suit

    # NOT INCLUDED IN UNIT TESTS
    def __str__(self)-> str:
        return f"{self.value_to_str()} of {self.suit_to_str()}"

    def __gt__(self, other : 'Card')-> bool:
        if type(other) is not Card:
            raise TypeError
        if self.value == other.value and self.suit > other.suit:    # same value, larger suit
            return True
        if self.value > other.value:    # larger value
            return True
        return False

    def __eq__(self, other : 'Card')-> bool:
        if type(other) is not Card:
            raise TypeError
        if self.value == other.value and self.suit == other.suit:
            return True
        return False


    # a dictionary would be more fitting
    def value_to_str(self)-> str:
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

    def suit_to_str(self)-> str:
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
    def verify_value(value: int)-> None:
        """verifies the value of the object"""
        if type(value) is not int:
            raise TypeError
        if not 1 <= value <= 13:
            raise ValueError

    @staticmethod
    def verify_suit(suit: int)-> None:
        """verifies the suit of the object"""
        if type(suit) is not int:
            raise TypeError
        if not 1 <= suit <= 4:
            raise ValueError