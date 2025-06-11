import unittest
from bowling import bowling_score

class TestBowlingScore(unittest.TestCase):
    def test_scores_0(self):
        self.assertEqual(bowling_score(""), 0)
    
    def test_scores_one_frame(self):
        self.assertEqual(bowling_score("45"), 9)
        self.assertEqual(bowling_score("33"), 6)
        self.assertEqual(bowling_score("53"), 8)

    def test_score_one_spare(self):
        self.assertEqual(bowling_score("6/ 42"), 20)
        self.assertEqual(bowling_score("3/ 71"), 25)
        self.assertEqual(bowling_score("8/ 52"), 22)

    def test_score_multiple_spares(self):    
        self.assertEqual(bowling_score("8/ 2/ 33"), 31)

    def test_score_non_consecutive_strikes(self):
        self.assertEqual(bowling_score("X"), 10)
        self.assertEqual(bowling_score("X 43 2/ 33"), 43)
        self.assertEqual(bowling_score("X 43 X"), 34)
        
    