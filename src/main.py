"""
Phan Vu Anh Minh
Guessing Game Project
Copyright 2022
"""
import sys
from os import path
import logging
from game import Game
import argparse
from config import GAME_DESCRIPTION

PACKAGE_PATH = path.realpath(path.join(path.dirname(__file__), '..'))
sys.path.append(PACKAGE_PATH)

logger = logging.getLogger(__name__)
parser = argparse.ArgumentParser(description=GAME_DESCRIPTION)
parser.parse_args()

def main():
    """
    center function to run the game
    """
    logging.basicConfig(format='%(asctime)s %(levelname)8s' +
                               ' (%(filename)s:%(lineno)s) --- %(message)s',
                        filename='../log/game.log',
                        filemode='a',
                        level=logging.INFO)

    logger.info('Game Started')
    game = Game()
    game.new_game()
    logger.info('Game ended')

if __name__ == '__main__':
    main()