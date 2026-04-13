# https://github.com/AlbertoR2026/lab-11-WT-AR
# Partner 1: William Tong
# Partner 2: Alberto Rios
import calculator

print("Running test cases")
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)

    ##########################

    ######## Partner 1

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,4), 12)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3,4), 2)

    ##########################

    ######## Partner 2 (alberto)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 100), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)

    ##########################

    ######## Partner 1

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-1, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(4, 6), 4)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(3), 4)
        with self.assertRaises(ValueError):
            square_root(-1)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
