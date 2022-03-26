from math_puzzle.arithmetric import Arithmetic

import unittest
from unittest.mock import patch
import random

class Arithmetic_GetAnswerTest(unittest.TestCase):

    def test_random_multiplication_0_to_10_must_be_in_0_to_100(self):
        ari = Arithmetic(min_num=0, max_num=10)
        ari.get_multiplication_question()
        result = ari.get_answer()
        expected_result = [int(x) for x in range(101)] 
        self.assertIn(result, expected_result)

    def test_random_addition_0_to_20_must_be_in_0_to_40(self):
        ari = Arithmetic(min_num=0, max_num=20)
        ari.get_addition_question()
        result = ari.get_answer()
        expected_result = [int(x) for x in range(41)]  
        self.assertIn(result, expected_result)

    def test_random_subtraction_0_to_50_must_be_in_0_to_50(self):
        ari = Arithmetic(min_num=0, max_num=50)
        ari.get_subtraction_question()
        result = ari.get_answer()
        expected_result = [int(x) for x in range(51)]  
        self.assertIn(result, expected_result)

    def test_random_division_0_to_100_must_be_in_0_to_100(self):
        ari = Arithmetic(min_num=0, max_num=100)
        ari.get_subtraction_question()
        result = ari.get_answer()
        expected_result = [int(x) for x in range(101)]  
        self.assertIn(result, expected_result)

    def test_random_modulus_0_to_20_must_be_in_0_to_10(self):
        ari = Arithmetic(min_num=0, max_num=20)
        ari.get_modulus_question()
        result = ari.get_answer()
        expected_result = [int(x) for x in range(10)]  
        self.assertIn(result, expected_result)

    def test_random_addition_0_to_20_not_in_0_to_n10(self):
        ari = Arithmetic(min_num=0, max_num=20)
        ari.get_addition_question()
        result = ari.get_answer()
        expected_result = [int(x) for x in range(0,21,-1)]  
        self.assertNotIn(result, expected_result)

    def test_random_subtraction_0_to_10_not_in_11_to_20(self):
        ari = Arithmetic(min_num=0, max_num=10)
        ari.get_subtraction_question()
        result = ari.get_answer()
        expected_result = [int(x) for x in range(11,21)]  
        self.assertNotIn(result, expected_result)

    def test_random_multiplication_0_to_10_not_in_101_to_1000(self):
        ari = Arithmetic(min_num=0, max_num=10)
        ari.get_multiplication_question()
        result = ari.get_answer()
        expected_result = [int(x) for x in range(101, 1001)] 
        self.assertNotIn(result, expected_result)


