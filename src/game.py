from entity import Player
from match import Match
from error import InvalidNameChoice, InvalidContinueChoice
import re
import logging

logger = logging.getLogger(__name__)

class Game:
    def new_game(self):
        logger.info('Create new player')
        player = self.create_player()
        match = Match(player)
        match.isPlaying = True
        while match.result() == 0:
            player.score = player.score-25
            match.start()
        if match.result() == 1:
            logger.info('Player wins')
            print(f'{player.name} is a winner!')
        if match.result() == -1:
            logger.info('Player loses')
            print(f"{player.name} lost this game :(")

    def create_player(self) -> Player:
        while True:
            try:
                prompt = "Show card as graphic? (Y/N) "
                showGraphics = input(prompt).strip().capitalize()
                if showGraphics not in ['Y', 'N']:
                    raise InvalidContinueChoice(showGraphics)
                break
            except InvalidContinueChoice as e:
                print(e)
                logger.exception('Player typed an invalid response')
        player_graphics = True if showGraphics == 'Y' else False
        
        while True:
            try:
                prompt = "Enter a name for this player (Only alphanumeric characters allowed): "
                name = input(prompt).strip()
                if name == "":
                    break
                if re.match(r'\W', name):
                    raise InvalidNameChoice(name)
                break
            except InvalidNameChoice as e:
                print(e)
        
        if name == "":
            return Player(player_graphics)
        return Player(player_graphics, name)


