# https://github.com/kwongosint/lab11-KW-CC
# Partner 1: Connor Corr
# Partner 2: Katie Wong


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    def test_add(self): # 3 assertions
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)

    # def test_subtract(self): # 3 assertions
    #     fill in code
    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-5, -5), 0)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
    def test_multiply(self):
        self.assertEqual(mul(10,5), 50)
        self.assertEqual(mul(-1,1), -1)
        self.assertEqual(mul(0,5),0)

    # def test_divide(self): # 3 assertions
    #     fill in code
    def test_divide(self):
        self.assertEqual(div(10,2),5)
        self.assertEqual(div(-10,2),-5)
        self.assertEqual(div(5, 2), 2.5)

    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ValueError):
            div(10, 0)

    # def test_logarithm(self): # 3 assertions
    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(8, 2), 3.0)
        self.assertAlmostEqual(log(100, 10), 2.0)
        self.assertAlmostEqual(log(1, 10), 0.0)

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(10, 1) 
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0,10)
    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4),5.0)
        self.assertEqual(hypotenuse(5,12),13.0)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.41421356)
    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    def test_sqrt(self):
        self.assertEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(2), 1.41421356)
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()