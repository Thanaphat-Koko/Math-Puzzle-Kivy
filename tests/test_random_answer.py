from math_puzzle.arithmetric import Arithmetic

import unittest
from unittest.mock import patch
import random

class Arithmetic_GetAnswerTest(unittest.TestCase):

    def test_random_multiplication_0_to_10_must_be_in_0_to_100(self):
        ari = Arithmetic(min_num=0, max_num=10)
        ari.get_multiplication_question()
        result = ari.get_answer()
        expected_result = [int(x) for x in range(100)]  #! 0 -> 100
        self.assertIn(result, expected_result)


