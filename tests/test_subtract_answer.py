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