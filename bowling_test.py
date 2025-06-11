import unittest
from bowling import bowling_score

class TestBowlingScore(unittest.TestCase):
    def test_scores_0(self):
        self.assertEqual(bowling_score(""), 0)
    

    