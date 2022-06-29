'''
1 match has multiple rounds
'''
from error import *
from cardset import CardSet
from entity import *
from card import GraphicDecorator
import logging

logger = logging.getLogger(__name__)
class Round:
    def __init__(self, player: Player) -> None:
        self._cardset = CardSet()
        self._multi = 0
        self._house = House()
        self._player = player
        self._roundNumber = 1
    
    def start(self):
        logger.info('Starting a new round')
        self._player.card, self._house.card, sign = self._cardset.get_cards()
        print(f'Starting round #{self._roundNumber}...')
        
        print("The House's card is ", end='')
        self.print_card(self._house)
        
        guess = self.valid_guess()
        logger.info('Player entered a guess')
        print(f"{self._player.name}'s card is ", end='')
        self.print_card(self._player)
        
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
        if self._player.showGraphics:
            print("\n" + str(GraphicDecorator(entity.card)))
        else:
            print(str(entity.card))

    def show_result(self, guess, sign):
        return (guess == '>' and sign) \
            or (guess == '<' and not sign)