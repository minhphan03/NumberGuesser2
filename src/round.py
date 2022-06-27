'''
1 match has multiple rounds
'''
from error import *
from cardset import CardSet
from entity import House, Player
class Round:
    def __init__(self, player: Player) -> None:
        self._cardset = CardSet()
        self._multi = 0
        self._house = House()
        self._player = player
        self._roundNumber = 1
    
    def start(self):
        p_card, h_card, sign = self._cardset.get_cards()
        self._player.set_card(p_card)
        self._house.set_card(h_card)
        print(f'Starting round #{self._roundNumber}...')
        print("The House's card is " + str(self._house.get_card()))
        prompt = "Type your guess: '>' for greater value and '<' otherwise: "
        
        while True:
            try:
                guess = input(prompt).strip()
                if guess not in ['>', '<']:
                    raise InvalidGuessChoice(guess)
                break
            except InvalidGuessChoice as e:
                print(e)
     
        print("Your card is " + str(self._player.get_card()))      
        if self.result(guess, sign):
            print("You won this round!")
            while True:
                try:
                    prompt = "Do you want to continue the next round? (Y/N) "
                    nextRound = input(prompt).strip().capitalize()
                    if nextRound not in ['Y', 'N']:
                        raise InvalidContinueChoice(nextRound)
                    break
                except InvalidContinueChoice as e:
                    print(e)
            
            if nextRound == 'Y':
                self._multi +=1
                self._roundNumber +=1
                self.start()
                # print statement
            else:
                # add points
                self._player.set_score(self._player.get_score() + 20*(2**self._multi))
                return
        else:
            print("Sorry, you've lost this match!")
            return
        
    def result(self, guess, sign: bool):
        return (guess == '>' and sign) \
            or (guess == '<' and not sign)
