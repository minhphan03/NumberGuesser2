"""
Configuration file, including constants used in other modules
"""

import logging

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
GROUPS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
SPECIALS = [('Black', 'Joker'), ('Red', 'Joker')]

SUITS_GRAPHIC = {
    'Spades': '♠',
    'Diamonds': '♦',
    'Hearts': '♥',
    'Clubs': '♣',
    'Red': 'R',
    'Black': 'B'
}

GROUPS_GRAPHIC = {
    'Ace': 'A ',
    '2': '2 ',
    '3': '3 ',
    '4': '4 ',
    '5': '5 ',
    '6': '6 ',
    '7': '7 ',
    '8': '8 ',
    '9': '9 ',
    '10': '10',
    'Jack': 'J ',
    'Queen': 'Q ',
    'King': 'K ',
    'Joker': 'JK'
}

GAME_DESCRIPTION = "Card Guessing Game by Minh Phan. \
    To play this game, type python main.py and follow the directions on the command line. \
    For further instructions, refer to the README.md file included in this game package."

def log_custom(func):
    """
    Logs a custom function into the log file
    """
    def log_func(*args):
        logging.info('Running {} with arguments {}'.format(func.__name__, args))
    return log_func

