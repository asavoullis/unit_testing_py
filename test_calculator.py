import unittest 
import calculator

# python -m unittest test_calculator.py

class TestCalculator(unittest.TestCase):

# https://docs.python.org/3/library/unittest.html    

    def test_add(self):
        # result = calculator.add(10, 5)
        # self.assertEqual(result, 15)
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)

if __name__ == '__main__':
    # now it can be run normally with this:
    unittest.main()