"""
Module to define a cardset for the game

"""
from card import Card
from config import SPECIALS, SUITS, GROUPS
import random

class CardSet:
    """
    A CardSet is a collection of all 54 cards included in a standard
    card set.
    """
    def __init__(self) -> None:
        """
        Initiates a set of 54 Card objects. 
        """
        self._cards = [Card(x, y) for x in GROUPS for y in SUITS]
        self._cards.extend(Card(x,y) for y, x in SPECIALS)

    def get_cards(self) -> tuple:
        """
        Return a three-element tuple,
        including two cards for the two sides of the game
        and a boolean value indicating their rank to each other.
        """
        c1, c2 = random.sample(self._cards, 2)
        sign = self.isGreater(c1, c2)
        return tuple([c1, c2, sign])

    def isGreater(self, card1: Card, card2: Card) -> bool:
        """
        Returns a boolean value indicating whether the first Card object
        has a greater value than the second Card object.
        """
        return self._cards.index(card1) > self._cards.index(card2)