from math_puzzle.arithmetric import Arithmetic
import unittest
from unittest.mock import patch

class Arithmetic_GetAnswerTest(unittest.TestCase):

    def test_1_plus_1_is_2(self):
            ari = Arithmetic()
            ari.num_one = 1
            ari.num_two = 1
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 2
            self.assertEqual(result, expected_output)
    
    def test_0_plus_0_is_0(self):
            ari = Arithmetic()
            ari.num_one = 0
            ari.num_two = 0
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 0
            self.assertEqual(result, expected_output)
    
    def test_24_plus_24_is_48(self):
            ari = Arithmetic()
            ari.num_one = 24
            ari.num_two = 24
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 48
            self.assertEqual(result, expected_output)

    def test_24_plus_0_is_24(self):
            ari = Arithmetic()
            ari.num_one = 24
            ari.num_two = 0
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 24
            self.assertEqual(result, expected_output)

    def test_0_plus_24_is_24(self):
            ari = Arithmetic()
            ari.num_one = 0
            ari.num_two = 24
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 24
            self.assertEqual(result, expected_output)

    def test_12_plus_12_is_24(self):
            ari = Arithmetic()
            ari.num_one = 12
            ari.num_two = 12
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 24
            self.assertEqual(result, expected_output)

    def test_10_plus_20_is_30(self):
            ari = Arithmetic()
            ari.num_one = 10
            ari.num_two = 20
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 30
            self.assertEqual(result, expected_output) 

    def test_5_plus_24_is_25(self):
            ari = Arithmetic()
            ari.num_one = 5
            ari.num_two = 24
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 29
            self.assertEqual(result, expected_output)

    def test_8_plus_19_is_27(self):
            ari = Arithmetic()
            ari.num_one = 8
            ari.num_two = 19
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 27
            self.assertEqual(result, expected_output)

    def test_5_plus_24_is_29(self):
            ari = Arithmetic()
            ari.num_one = 2
            ari.num_two = 22
            ari.operation = "+"
            result = ari.get_answer()
            expected_output = 24
            self.assertEqual(result, expected_output) 