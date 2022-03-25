from math_puzzle.arithmetric import Arithmetic
import unittest
import random

class Arithmetic_GetAnswerTest(unittest.TestCase):

    def test_10_modulus_2_is_0(self):
        ari = Arithmetic()
        ari.num_one = 10
        ari.num_two = 2
        ari.operation = "%"
        result = ari.get_answer()
        expected_output = 0
        self.assertEqual(result, expected_output)