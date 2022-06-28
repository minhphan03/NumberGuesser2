'''
1 match has multiple rounds
'''
from error import *
from cardset import CardSet
from entity import *
from card import GraphicDecorator

class Round:
    def __init__(self, player: Player) -> None:
        self._cardset = CardSet()
        self._multi = 0
        self._house = House()
        self._player = player
        self._roundNumber = 1
    
    def start(self):
        self._player.card = self._cardset.player_card
        self._house.card = self._cardset.house_card
        print(f'Starting round #{self._roundNumber}...')
        print("The House's card is ", end='')
        self.print_card(self._house)
        
        guess = self.valid_guess()

        print("Your card is ", end='')
        self.print_card(self._player)
        
        if self.show_result(guess):
            print("You won this round!")
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
            print("Sorry, you've lost this match!")
    
    def valid_guess(self) -> str:
        prompt = "Type your guess: '>' for greater value and '<' otherwise: "
        while True:
            try:
                guess = input(prompt).strip()
                if guess not in ['>', '<']:
                    raise InvalidGuessChoice(guess)
                break
            except InvalidGuessChoice as e:
                print(e)
    
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

    def print_card(self, entity: Entity):
        if self._player.showGraphics:
            print("\n" + str(GraphicDecorator(entity.card)))
        else:
            print(str(entity.card))

    def show_result(self, guess):
        sign = self._cardset.sign
        return (guess == '>' and sign) \
            or (guess == '<' and not sign)