import unittest
from bowling import bowling_score

class TestBowlingScore(unittest.TestCase):
    def test_scores_0(self):
        self.assertEqual(bowling_score(""), 0)
    
    def test_scores_x(self):
        self.assertEqual(bowling_score("X"), 10)
    
    def test_scores_45(self):
        self.assertEqual(bowling_score("45"), 9)