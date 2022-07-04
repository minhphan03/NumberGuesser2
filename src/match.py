"""
Module to define a match object
"""
from round import Round
from entity import Player
import logging

logger = logging.getLogger(__name__)

class Match:
    """
    An object representing a single match of the game
    """
    def __init__(self, player: Player) -> None:
        """
        Initiate a match with a Player instance to keep track of points
        """
        self._player = player
        self._match = 0
        self.isPlaying = False

    def start(self):
        """
        Start a match and keep track of the records in the said match
        """
        print(f"Player {self._player.name} currently have " + str(self._player.score) + " points.")
        round = Round(self._player)
        self._match +=1
        if self.isPlaying:
            print(f"Starting match {self._match}...")
            round.start()
    
    def result(self) -> int:
        """
        Return the player game condition after each match
        """
        if self._player.score >= 1000:
            return 1
        elif self._player.score < 25:
            return -1
        else:
            return 0
