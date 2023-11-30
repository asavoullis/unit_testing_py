import unittest 
import calculator

# python -m unittest test_calculator.py 
# (4 dots)

class TestCalculator(unittest.TestCase):

# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug 

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

    def test_divide_raises_error(self):
        # self.assertRaises(ValueError, calculator.divide, 10, 0)
        """ alterative way """
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    def test_floor_division(self):
        self.assertEqual(calculator.floor_division(10, 3), 3)
        self.assertEqual(calculator.floor_division(-10, 3), -4)
        self.assertEqual(calculator.floor_division(5, 2), 2)
    
    def test_floor_division_raises_error(self):
        # self.assertRaises(ValueError, calculator.floor_division, 10, 0)
        with self.assertRaises(ValueError):
            calculator.floor_division(10, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)
        self.assertEqual(calculator.power(5, 1), 5)
        self.assertEqual(calculator.power(5, -1), 1/5)

    def test_square_root(self):
        self.assertEqual(calculator.square_root(25), 5)
        self.assertEqual(calculator.square_root(0), 0)

        with self.assertRaises(ValueError):
            calculator.square_root(-1)
    
    def test_absolute_value(self):
        self.assertEqual(calculator.absolute_value(10), 10)
        self.assertEqual(calculator.absolute_value(-5), 5)
        self.assertEqual(calculator.absolute_value(0), 0)
        

if __name__ == '__main__':
    # now it can be run normally with this:
    unittest.main()