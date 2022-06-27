from round import Round
from entity import Player

class Match:
    def __init__(self, player: Player) -> None:
        self._player = player
        self._match = 0
        self.isPlaying = False

    def start(self):
        print("You currently have " + str(self._player.score) + " points.")
        round = Round(self._player)
        self._match +=1
        if self.isPlaying:
            print(f"Starting match {self._match}...")
            round.start()
    
    def result(self) -> int:
        if self._player.score >= 1000:
            return 1
        elif self._player.score < 25:
            return -1
        else:
            return 0
        
