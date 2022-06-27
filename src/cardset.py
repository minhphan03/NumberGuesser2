from card import Card
from config import SPECIALS, SUITS, GROUPS
import random

class CardSet:
    def __init__(self) -> None:
        self._cards = [Card(x, y) for x in GROUPS for y in SUITS]
        self._cards.extend(Card(x,y) for y, x in SPECIALS)
        self._player, self._house, self._sign = self.get_cards()

    def get_cards(self) -> tuple:
        c1, c2 = random.sample(self._cards, 2)
        sign = self.isGreater(c1, c2)
        return tuple([c1, c2, sign])

    def isGreater(self, card1: Card, card2: Card) -> bool:
        return self._cards.index(card1) > self._cards.index(card2)
    
    @property
    def player_card(self) -> Card:
        return self._player
    
    @property
    def house_card(self) -> Card:
        return self._house
    
    @property
    def sign(self) -> Card:
        return self._sign