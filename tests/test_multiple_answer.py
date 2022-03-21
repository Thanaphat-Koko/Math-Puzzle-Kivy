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

    def test_24_multiple_24_is_576(self):
            ari = Arithmetic()
            ari.num_one = 24
            ari.num_two = 24
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = [576]
            self.assertIn(result, expected_output) 
 

    def test_multiple_in_range_0_to_24_must_less_than_577(self):
        ari = Arithmetic(min_num=0, max_num=24)
        ari.get_multiplication_question()
        result = ari.get_answer()
        self.assertLess(result, 577)                           

    def test_15_multiple_3_is_45(self):
            ari = Arithmetic()
            ari.num_one = 15
            ari.num_two = 3
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 45
            x = result == expected_output
            self.assertTrue(x)    

    def test_24_multiple_0_is_0(self):
            ari = Arithmetic()
            ari.num_one = 24
            ari.num_two = 0
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 0
            self.assertEqual(result, expected_output)

    def test_0_multiple_24_is_0(self):
            ari = Arithmetic()
            ari.num_one = 0
            ari.num_two = 24
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 0
            self.assertEqual(result, expected_output)      

    def test_12_multiple_12_is_144(self):
            ari = Arithmetic()
            ari.num_one = 12
            ari.num_two = 12
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 144
            self.assertEqual(result, expected_output)          

    def test_10_multiple_20_is_200(self):
            ari = Arithmetic()
            ari.num_one = 10
            ari.num_two = 20
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 200
            self.assertEqual(result, expected_output)   

    def test_5_multiple_24_is_120(self):
            ari = Arithmetic()
            ari.num_one = 5
            ari.num_two = 24
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 120
            self.assertEqual(result, expected_output)             

    def test_8_multiple_19_is_152(self):
            ari = Arithmetic()
            ari.num_one = 8
            ari.num_two = 19
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 152
            self.assertEqual(result, expected_output)     

    def test_5_multiple_24_is_120(self):
            ari = Arithmetic()
            ari.num_one = 5
            ari.num_two = 24
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 120
            self.assertEqual(result, expected_output)           

    def test_8_multiple_9_is_72(self):
            ari = Arithmetic()
            ari.num_one = 8
            ari.num_two = 9
            ari.operation = "x"
            result = ari.get_answer()
            expected_output = 72
            self.assertEqual(result, expected_output)    