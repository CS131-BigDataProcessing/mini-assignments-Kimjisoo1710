import math
import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):

#power unit tests    
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(1/2, 2), 1/4)
        self.assertEqual(power(2, 1/2), math.sqrt(2))

    def test_power_zero(self):
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 3), 0)

    def test_power_negative(self):
        self.assertEqual(power(4, -3), 1/64)
        self.assertEqual(power(-4, 3), -64)
        self.assertEqual(power(-2, 4), 16)
        self.assertEqual(power(2, -4), 1/16)

    def test_power_large_values(self):
        large_num = 1e2
        self.assertEqual(power(large_num, large_num), 1e200)
        
#divide unit tests 
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(27, 3), 9)

    def test_divide_zero(self):
        self.assertEqual(divide(10, 0), "Cannot divide by 0")
        self.assertEqual(divide(0, 2), 0)
        self.assertEqual(divide(0, 0), "Cannot divide by 0")

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)
        self.assertAlmostEqual(divide(-2, 3), -2/3)
        self.assertAlmostEqual(divide(2, -3), -2/3)
        self.assertAlmostEqual(divide(-2, -3), 2/3)

    def test_divide_large_values(self):
        large_number = 1e100
        self.assertEqual(divide(large_number, large_number), 1)

if __name__ == '__main__':
    unittest.main()

