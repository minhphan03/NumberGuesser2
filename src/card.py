from config import GROUPS_GRAPHIC, SUITS_GRAPHIC

class Card:
    def __init__(self, group, suit) -> None:
        self._suit = suit
        self._group = group
    
    def get_suit(self):
        return self._suit
    
    def get_group(self):
        return self._group

    def __str__(self) -> str:
        return self._group + " " + self._suit

    def __eq__(self, __o: object) -> bool:
        return self._suit == __o._suit and self._group == __o._group

class Decorator(Card):
    _card: Card = None

    def __init__(self, card: Card) -> None:
        self._card = card
    
    @property
    def card():
        return self._card
    
    def __str__(self):
        return self._card.__str__()

class GraphicDecorator(Decorator):
    def __str__(self):
        lines = []
        # print a card
        lines[0] = '┌────────┐'
        lines[1] = '│{}     │'.format(GROUPS_GRAPHIC[self.get_group()])
        lines[2] = '│       │'
        lines[3] = '│   {}   │'.format(SUITS_GRAPHIC[self.get_suit()])
        lines[4] = '│        │'
        lines[5] = '│     {}│'.format(GROUPS_GRAPHIC[self.get_group()])
        lines[6] = '└────────┘'