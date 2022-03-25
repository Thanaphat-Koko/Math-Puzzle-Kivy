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
    
    def test_25_modulus_4_is_1(self):
        ari = Arithmetic()
        ari.num_one = 25
        ari.num_two = 4
        ari.operation = "%"
        result = ari.get_answer()
        expected_output = 1
        self.assertEqual(result, expected_output)
    
    def test_15_modulus_15_is_0(self):
        ari = Arithmetic()
        ari.num_one = 15
        ari.num_two = 15
        ari.operation = "%"
        result = ari.get_answer()
        expected_output = 0
        self.assertEqual(result, expected_output)

    def test_0_modulus_5_is_0(self):
        ari = Arithmetic()
        ari.num_one = 0
        ari.num_two = 5
        ari.operation = "%"
        result = ari.get_answer()
        expected_output = 0
        self.assertEqual(result, expected_output)

    def test_20_modulus_25_is_20(self):
        ari = Arithmetic()
        ari.num_one = 20
        ari.num_two = 25
        ari.operation = "%"
        result = ari.get_answer()
        expected_output = 20
        self.assertEqual(result, expected_output)

    def test_negative_5_modulus_2_is_1(self):
        ari = Arithmetic()
        ari.num_one = -5
        ari.num_two = 2
        ari.operation = "%"
        result = ari.get_answer()
        expected_output = 1
        self.assertEqual(result, expected_output)

    def test_37_modulus_negative_5_is_negative_3(self):
        ari = Arithmetic()
        ari.num_one = 37
        ari.num_two = -5
        ari.operation = "%"
        result = ari.get_answer()
        expected_output = -3
        self.assertEqual(result, expected_output)

    def test_40_modulus_8_should_less_than_8(self):
        ari = Arithmetic()
        ari.num_one = 40
        ari.num_two = 8
        ari.operation = "%"
        result = ari.get_answer()
        expected_output = 8
        self.assertLess(result, expected_output)