import unittest
from bowling import bowling_score

class TestBowlingScore(unittest.TestCase):
    def test_0(self):
        self.assertEqual(bowling_score(""), 0)
    
    def test_one_open_frame(self):
        self.assertEqual(bowling_score("45"), 9)
        self.assertEqual(bowling_score("33"), 6)
        self.assertEqual(bowling_score("53"), 8)

    def test_one_spare(self):
        self.assertEqual(bowling_score("6/ 42"), 20)
        self.assertEqual(bowling_score("3/ 71"), 25)
        self.assertEqual(bowling_score("8/ 52"), 22)

    def test_multiple_spares(self):    
        self.assertEqual(bowling_score("8/ 2/ 33"), 31)

    def test_non_consecutive_strikes(self):
        self.assertEqual(bowling_score("X"), 10)
        self.assertEqual(bowling_score("X 43 2/ 33"), 43) # this is not a non-consecutive strike
        self.assertEqual(bowling_score("X 43 X"), 34)
        
    def test_one_strike_followed_by_spare(self):
        self.assertEqual(bowling_score("X 8/ 2/ 33"), 51)

    def test_one_spare_followed_by_strike(self):
        self.assertEqual(bowling_score("8/ X"), 30)
        self.assertEqual(bowling_score("53 42 8/ X"), 44)

    def test_double_strikes(self):
        self.assertEqual(bowling_score("X X 52 11 11"), 53)
        self.assertEqual(bowling_score("X X 5/ 11"), 58)
        self.assertEqual(bowling_score("X X 52"), 49)

    def test_two_plus_strikes_middle_game(self):
        self.assertEqual(bowling_score("X X X 52"),79)
        self.assertEqual(bowling_score("X X X X 52"),109)
        self.assertEqual(bowling_score("X X X X X 52"),139)

        
        