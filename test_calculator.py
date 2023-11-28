import unittest 
import calculator

# python -m unittest test_calculator.py 
# (4 dots)

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

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1, -1), 1)
        self.assertEqual(calculator.divide(5, 2), 2.5)

    def test_floor_division(self):
        self.assertEqual(calculator.floor_division(10, 3), 3)
        self.assertEqual(calculator.floor_division(-10, 3), -4)
        self.assertEqual(calculator.floor_division(5, 2), 2)



if __name__ == '__main__':
    # now it can be run normally with this:
    unittest.main()