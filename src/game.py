PLAYER_SCORE = 60
from entity import Player
from match import Match

def new_game():
    player = Player()
    match = Match(player)
    match.isPlaying = True
    while match.result() == 0:
        player.set_score(player.get_score()-25)
        match.start()
    if match.result() == 1:
        print("You win!")
    if match.result() == -1:
        print("Sorry you've lost")

if __name__ == '__main__':
    new_game()
