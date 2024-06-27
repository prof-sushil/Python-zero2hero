# First we should import the unittest module
import unittest

# This is the function we want to test
def div(x, y):
    return x / y

# Create a class that inherits from unittest.TestCase
class TestDiv(unittest.TestCase):
    # We will write tests here which will test the vulnerable function
    def test_div_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)
        
    def test_div_pass(self):
        self.assertEqual(div(1, 1), 1)
        self.assertGreaterEqual(div(1, 2), 0.5)
        
    def test_div_fail(self):
        self.assertEqual(div(1, 1), 2)

if __name__ == '__main__':
    unittest.main()