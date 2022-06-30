import logging
from game import Game

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)8s' +
                               ' (%(filename)s:%(lineno)s) --- %(message)s',
                        filename='log/game.log',
                        filemode='a',
                        level=logging.INFO)

    logger.info('Game Started')
    game = Game()
    game.new_game()
    logger.info('Game ended')

if __name__ == '__main__':
    main()