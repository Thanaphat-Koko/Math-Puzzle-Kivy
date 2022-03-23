from math_puzzle.arithmetric import Arithmetic
import unittest
from unittest.mock import patch

class Arithmetic_GetAnswerTest(unittest.TestCase):

    def test_1_divided_by_1_is_1(self):
            ari = Arithmetic()
            ari.num_one = 1
            ari.num_two = 1
            ari.operation = "÷"
            result = ari.get_answer()
            expected_output = 1
            self.assertEqual(result, expected_output)

    def test_0_divided_by_0_is_Divided_by_Zero(self):
            ari = Arithmetic()
            ari.num_one = 0
            ari.num_two = 0
            ari.operation = "÷"
            result = ari.get_answer()
            expected_output = "Divided by Zero"
            self.assertEqual(result, expected_output)

    def test_24_divided_by_24_is_1(self):
            ari = Arithmetic()
            ari.num_one = 24
            ari.num_two = 24
            ari.operation = "÷"
            result = ari.get_answer()
            expected_output = 1
            self.assertEqual(result, expected_output)

    def test_24_divided_by_0_is_Divided_by_Zero(self):
            ari = Arithmetic()
            ari.num_one = 24
            ari.num_two = 0
            ari.operation = "÷"
            result = ari.get_answer()
            expected_output = "Divided by Zero"
            self.assertEqual(result, expected_output)

    def test_0_divided_by_24_is_0(self):
            ari = Arithmetic()
            ari.num_one = 0
            ari.num_two = 24
            ari.operation = "÷"
            result = ari.get_answer()
            expected_output = 0
            self.assertEqual(result, expected_output)

    def test_12_divided_by_12_is_1(self):
            ari = Arithmetic()
            ari.num_one = 12
            ari.num_two = 12
            ari.operation = "÷"
            result = ari.get_answer()
            expected_output = 1
            self.assertEqual(result, expected_output)

    def test_10_divided_by_20_is_Error(self):
            ari = Arithmetic()
            ari.num_one = 10
            ari.num_two = 20
            ari.operation = "÷"
            result = ari.get_answer()
            expected_output = "Error"
            self.assertEqual(result, expected_output)

    def test_24_divided_by_8_is_3(self):
            ari = Arithmetic()
            ari.num_one = 24
            ari.num_two = 8
            ari.operation = "÷"
            result = ari.get_answer()
            expected_output = 3
            self.assertEqual(result, expected_output)

    def test_16_divided_by_8_is_2(self):
            ari = Arithmetic()
            ari.num_one = 16
            ari.num_two = 8
            ari.operation = "÷"
            result = ari.get_answer()
            expected_output = 2
            self.assertEqual(result, expected_output)