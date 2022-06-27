from io import StringIO
import unittest
import os.path, sys
from unittest.mock import Mock, patch, PropertyMock
from contextlib import redirect_stdout

PACKAGE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
SRC = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(SRC)
sys.path.append(PACKAGE_PATH)

from entity import Player
from card import Card
from match import Match
from round import Round

class MockTestMethods(unittest.TestCase):
    # test calls to a method
    def test_player(self):
        mock_player = Mock()
        mock_player.get_score.return_value = 100
        match = Match(mock_player)
        result = match.result()
        self.assertEqual(mock_player.get_score.call_count, 2)
        # self.assertFalse(mock_player.result())
        # print(mock_player.result())

    # mock test the round object
    @patch('builtins.input', return_value='<')
    def test_round(self, _input):
        player = Player()
        round = Round(player)
        f = StringIO()
        with patch.object(round, '_cardset', new_callable=PropertyMock) as obj_mock:
            # assertFalse for wrong 
            with redirect_stdout(f):
                obj_mock.player_card.return_value = Card('10', 'Spades')
                obj_mock.house_card.return_value = Card('King', 'Hearts')
                obj_mock.sign.return_value = True
                round.start()
                self.assertEqual("Starting round #1...\n"\
                    "The House's card is King Hearts\n"\
                    "Your card is 10 Spades\n"\
                    "Sorry, you've lost this match!\n", f.getvalue())
            

if __name__ == "__main__":
    unittest.main()
    # print(sys.path)