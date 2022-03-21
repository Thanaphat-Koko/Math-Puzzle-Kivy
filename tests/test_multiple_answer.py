from math_puzzle.arithmetric import Arithmetic
import unittest
from unittest.mock import patch

class Arithmetic_GetAnswerTest(unittest.TestCase):

    def test_1_multiple_1_is_1(self):
            ari = Arithmetic()
            ari.num_one = 1
            ari.num_two = 1
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 1
            self.assertEqual(result, expected_output)

    def test_0_multiple_0_is_0(self):
            ari = Arithmetic()
            ari.num_one = 0
            ari.num_two = 0
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 0
            self.assertIs(result, expected_output)        