import unittest 
import calculator

# python -m unittest test_calculator.py

class TestCalculator(unittest.TestCase):

# https://docs.python.org/3/library/unittest.html    

    def test_add(self):
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)



if __name__ == '__main__':
    unittest.main()