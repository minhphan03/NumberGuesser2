from game import Game
import logging
import logging

def log_custom(func):
    def log_func(*args):
        logging.info('Running {} with arguments {}'.format(func.__name__, args))

def main():
    # root logger
    logging.basicConfig(format='%(asctime)s %(levelname)8s' +
                               ' (%(filename)s:%(lineno)s) --- %(message)s',
                        filename='../log/game.log',
                        filemode='a',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('Game Started')
    game = Game()
    game.new_game()
    logger.info('Game ended')

if __name__ == '__main__':
    main()