import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ this basically means that we are working with a class rather than the instance of the class like self """
        """ runs before anything (in the beginning of the script ) useful if you want to do something once """
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        """ runs after everything (in the end of the script ) useful if you want to do something once (maybe its too costly to do before every test )"""
        print('teardownClass')

    def setUp(self):
        """ this will run before every single test """
        # in order to access these from without our other tests use self.
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        """ this will run after every single test """
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_repr(self):
        print('test_repr')
        self.assertEqual(repr(self.emp_1), "Employee('Corey', 'Schafer', 50000, 'Corey.Schafer@email.com')")
        self.assertEqual(repr(self.emp_2), "Employee('Sue', 'Smith', 60000, 'Sue.Smith@email.com')")

    def test_str(self):
        print('test_str')
        self.assertEqual(str(self.emp_1), 'Corey Schafer - $50000 - Corey.Schafer@email.com')
        self.assertEqual(str(self.emp_2), 'Sue Smith - $60000 - Sue.Smith@email.com')

    def test_add(self):
        print('test_add')
        total = self.emp_1 + self.emp_2

        self.assertEqual(total, 110000)
    
    def test_attribute_length(self):
        self.assertEqual(self.emp_1.attribute_length('name'), 5)
        self.assertEqual(self.emp_1.attribute_length('name'), len(self.emp_1.first))
        self.assertEqual(self.emp_2.attribute_length('first'), 3)
        self.assertEqual(self.emp_2.attribute_length('first'), len(self.emp_2.first))

        self.assertEqual(self.emp_1.attribute_length('fullname'), 13)
        self.assertEqual(self.emp_1.attribute_length('fullname'), len(self.emp_1.fullname))

        self.assertEqual(self.emp_1.attribute_length('surname'), 7)
        self.assertEqual(self.emp_2.attribute_length('surname'), len(self.emp_2.last))

        self.assertEqual(self.emp_1.attribute_length('last'), 7)
        self.assertEqual(self.emp_1.attribute_length('last'), len(self.emp_1.last))
        
        self.assertEqual(self.emp_1.attribute_length('email'), len(self.emp_1.email))
        self.assertEqual(self.emp_1.attribute_length('email'), len(self.emp_1.first)+len(self.emp_1.last)+len(".@gmail.com"))
        self.assertEqual(self.emp_1.attribute_length('email'), 23)

        with self.assertRaises(ValueError):
            self.emp_1.attribute_length('invalid_attribute')


    """ let's say we have a function that goes to a website and pulls down some information """

if __name__ == '__main__':
    unittest.main()