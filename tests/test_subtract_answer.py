from math_puzzle.arithmetric import Arithmetic
import unittest
from unittest.mock import patch

class Arithmetic_GetAnswerTest(unittest.TestCase):

    def test_1_subtract_1_is_0(self):
            ari = Arithmetic()
            ari.num_one = 1
            ari.num_two = 1
            ari.operation = "-"
            result = ari.get_answer()
            expected_output = 0
            self.assertEqual(result, expected_output)
    
    def test_subtract_in_range_0_to_24_must_less_than_25(self):
        ari = Arithmetic(min_num=0, max_num=24)
        ari.get_subtraction_question()
        result = ari.get_answer()
        self.assertLess(result, 25)

    def test_24_subtract_24_is_0(self):
            ari = Arithmetic()
            ari.num_one = 24
            ari.num_two = 24
            ari.operation = "-"
            result = ari.get_answer()
            expected_output = 0
            x = result == expected_output
            self.assertTrue(x)