from config import GROUPS_GRAPHIC, SUITS_GRAPHIC

class Card:
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
        return self._group + " " + self._suit

class Decorator(Card):
    def __init__(self, card: Card) -> None:
        self._card = card
    
    def __str__(self):
        return self._card.__str__()

class GraphicDecorator(Decorator):
    def __str__(self):
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