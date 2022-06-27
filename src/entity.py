import random
from card import Card

class Entity:
    def __init__(self) -> None:
        self._card = None
    
    def set_card(self, card:Card):
        self._card = card

    def get_card(self) -> Card:
        return self._card


class House(Entity):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        super().start()


class Player(Entity):
    def __init__(self) -> None:
        super().__init__()
        self._score = 60

    def result(self) -> bool:
        if self.get_score() < 25:
            print("Sorry, you've lost this game")
            return True
        elif self.get_score() >= 1000:
            print("You winnnnnnn!")
            return True
        else:
            return False

    def get_score(self) -> int:
        return self._score
    
    def set_score(self, new_score: int):
        self._score = new_score
    