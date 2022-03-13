from math_puzzle.arithmetric import Arithmetic

import unittest
from unittest.mock import patch
import random

class Arithmetic_GetAnswerTest(unittest.TestCase):

    # @patch('math_puzzle.arithmetric.Arithmetic.get_answer', return_value = 10)
    def test_random_multiplication_0_to_10_must_less_than_101(self):
        ari = Arithmetic(min_num=0, max_num=10)
        ari.get_multiplication_question()
        result = ari.get_answer()
        self.assertLess(result, 101)
