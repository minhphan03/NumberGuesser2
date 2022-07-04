"""
Module to define the player and the house object in the game
"""
from card import Card

class Entity:
    """
    An abstract class to define a general entity (side)
    in the game.
    """
    def __init__(self) -> None:
        """
        An entity always holds a card.
        """
        self._card = None

    @property
    def card(self) -> Card:
        return self._card
    
    @card.setter
    def card(self, card:Card):
        self._card = card


class House(Entity):
    """
    The house is played by the "computer"
    in the game. The house does not hold points.
    """
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        super().start()


class Player(Entity):
    """
    A Player is played by the human interacting with the command line.
    """
    def __init__(self, showGraphics=False, name='Anonymous') -> None:
        """
        Given the name and their choice of showing the cards graphically (drawing)
        initiates an entity with starting point of 60 points, a user-defined name
        and the option to show the graphic, which is consistent throughout the game.
        """
        super().__init__()
        self._name = name
        self._score = 60
        self._showGraphics = showGraphics

    def result(self) -> bool:
        """
        A player wins if they have 1000 points after any single match,
        and loses if they have below 25 points. 
        """
        if self.get_score() < 25:
            print("Sorry, you've lost this game")
            return True
        elif self.get_score() >= 1000:
            print("You winnnnnnn!")
            return True
        else:
            return False
    
    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, new_score: int):
        self._score = new_score
    
    @property
    def showGraphics(self) -> bool:
        return self._showGraphics
    
    @property
    def name(self):
        return self._name
    