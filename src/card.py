"""
Module to define a card object
"""
from config import GROUPS_GRAPHIC, SUITS_GRAPHIC

class Card:
    """
    A card object defines methods to print information,
    return properties to help with comparison of a single card.
    """
    def __init__(self, group, suit) -> None:
        self._suit = suit
        self._group = group
    
    @property
    def suit(self):
        return self._suit
    
    @property
    def group(self):
        return self._group

    def __str__(self) -> str:
        """
        Print out the details of the card in literal strings
        """
        return self._group + " " + self._suit

class Decorator(Card):
    """
    An abstract class to decorate a card object.
    Implemented using the Decorator design pattern
    """
    def __init__(self, card: Card) -> None:
        self._card = card
    
    def __str__(self):
        return self._card.__str__()

class GraphicDecorator(Decorator):
    """
    A concrete class implemented based on the details
    of the Decorator abstract class.
    """
    def __str__(self):
        """
        Prints out the card in the shape of a card on the command line
        """
        lines = []
        # print a card
        lines.append('┌────────┐')
        lines.append('│{}      │'.format(GROUPS_GRAPHIC[self._card.group]))
        lines.append('│        │')
        lines.append('│   {}    │'.format(SUITS_GRAPHIC[self._card.suit]))
        lines.append('│        │')
        lines.append('│      {}│'.format(GROUPS_GRAPHIC[self._card.group]))
        lines.append('└────────┘')
        return "\n".join(lines)