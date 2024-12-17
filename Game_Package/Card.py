# a class representing a  single card in a deck of 52 cards.
# each card has a suit from 1 to 4, and a value from 1 to 13.
class Card:
    def __init__(self, suit: int, value: int)-> None:
        """gets two int values and creates an object"""
        self.verify_suit(suit)
        self.verify_value(value)
        self.value = value
        self.suit = suit
        self.value_to_str_dict = self.value_to_str()
        self.suit_to_str_dict = self.suit_to_str()

    # NOT INCLUDED IN UNIT TESTS
    def __str__(self)-> str:
        return f"{self.value_to_str_dict[self.value]} of {self.suit_to_str_dict[self.suit]}"

    def __gt__(self, other : 'Card')-> bool:
        if type(other) is not Card:
            raise TypeError("object for comparison type is not card")
        if self.value == other.value and self.suit > other.suit:    # same value, larger suit
            return True
        return self.value > other.value    # larger value

    def __eq__(self, other : 'Card')-> bool:
        if type(other) is not Card:
            raise TypeError("object for comparison type is not card")
        return self.value == other.value and self.suit == other.suit


    @staticmethod
    def value_to_str()-> dict:
        """returns the string associated with the value of the card"""
        return {
            1 : "Two",
            2 : "Three",
            3 : "Four",
            4 : "Five",
            5 : "Six",
            6 : "Seven",
            7 : "Eight",
            8 : "Nine",
            9 : "Ten",
            10 : "Jack",
            11 : "Queen",
            12 : "King",
            13 : "Ace"
        }

    @staticmethod
    def suit_to_str()-> dict:
        """returns the string associated with the suit of the card"""
        return {
            1: "Diamonds",
            2: "Spades",
            3: "Hearts",
            4: "Clubs"
        }

    @staticmethod
    def verify_value(value: int)-> None:
        """verifies the value of the object"""
        if type(value) is not int:
            raise TypeError("value type is not of int")
        if not 1 <= value <= 13:
            raise ValueError("value value is not 1 <= value <= 13")

    @staticmethod
    def verify_suit(suit: int)-> None:
        """verifies the suit of the object"""
        if type(suit) is not int:
            raise TypeError("suit type is not int")
        if not 1 <= suit <= 4:
            raise ValueError("suit value is not 1 <= value <= 4")