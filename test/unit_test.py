import unittest
import io
import sys
import os
from contextlib import redirect_stdout

SRC = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(SRC)

from match import Match
from entity import Player

class UnitTestMethods(unittest.TestCase):
    def testWinCondition(self):
        player = Player()
        player.score = 1000
        match = Match(player)
        self.assertEqual(1, match.result())
    
    def testLostCondition(self):
        player = Player()
        player.score = 24
        match = Match(player)
        self.assertEqual(-1, match.result())
    
    def testMatch(self):
        f = io.StringIO()
        # capture all console output for testing
        with redirect_stdout(f):
            player = Player()
            match = Match(player)
            match.start()
        # print("test output is", f.getvalue())
        self.assertEqual("You currently have 60 points.\n", f.getvalue())

if __name__ == "__main__":
    unittest.main()