'''
Round module to define a round object
'''
from error import *
from cardset import CardSet
from entity import *
from card import GraphicDecorator
from config import log_custom
import logging

logger = logging.getLogger(__name__)

class Round:
    """
    A round instance makes up one of many of a single match of the game.
    Each round prompts the player to enter the guess and based on the result,
    will either ask them to continue playing or stop, or end the match if lost
    """
    def __init__(self, player: Player) -> None:
        """
        Initiate the object with a Player instance to keep track of the points
        of the said player
        """
        self._cardset = CardSet()
        self._multi = 0
        self._house = House()
        self._player = player
        self._roundNumber = 1
    
    def start(self):
        """
        Start the round, prompt the questions and direct the next rounds 
        of a single match recursively.
        """
        logger.info('Starting a new round')
        self._player.card, self._house.card, sign = self._cardset.get_cards()
        print(f'Starting round #{self._roundNumber}...')
        
        print("The House's card is ", end='')
        self.print_card(self._house)
        
        guess = self.valid_guess()
        logger.info('Player entered a guess')
        print(f"{self._player.name}'s card is ", end='')
        self.print_card(self._player)
        log = log_custom(self.show_result)
        log(guess, sign)
        if self.show_result(guess, sign):
            logger.info('Player won this round')
            print(f"{self._player.name} won this round!")
            nextRound = self.valid_choice()
            if nextRound == 'Y':
                self._multi +=1
                self._roundNumber +=1
                # start another round
                self.start()
            else:
                # add points
                self._player.score = self._player.score + 20*(2**self._multi)
        else:
            logger.info('Player lost this round')
            print(f"Sorry, {self._player.name} lost this round :(")
    
    def valid_guess(self) -> str:
        """
        Displays the question for the player to guess
        and checks whether the guess is correct or not.
        Returns a response ('>' or '<') indicating the player's guess
        whether their card is larger or smaller than that of the house.
        """
        prompt = f"Type {self._player.name}'s guess: '>' for greater value and '<' otherwise: "
        while True:
            try:
                guess = input(prompt).strip()
                if guess not in ['>', '<']:
                    raise InvalidGuessChoice(guess)
                break
            except InvalidGuessChoice as e:
                print(e)
                logger.exception('Player typed an invalid response')
        return guess

    def valid_choice(self) -> str:
        """
        Checks that in case the player wins, they want to continue or not.
        Returns an appropriate response (string) to process the game further.
        """
        while True:
            try:
                prompt = "Do you want to continue the next round? (Y/N) "
                nextRound = input(prompt).strip().capitalize()
                if nextRound not in ['Y', 'N']:
                    raise InvalidContinueChoice(nextRound)
                break
            except InvalidContinueChoice as e:
                print(e)
                logger.exception('Player typed an invalid response')
        return nextRound

    def print_card(self, entity: Entity):
        """
        Given the entity (house or player),
        prints the cards of the round.
        """
        if self._player.showGraphics:
            print("\n" + str(GraphicDecorator(entity.card)))
        else:
            print(str(entity.card))

    def show_result(self, guess, sign):
        """
        Checks that whether the player's guess is correct.
        """
        return (guess == '>' and sign) \
            or (guess == '<' and not sign)