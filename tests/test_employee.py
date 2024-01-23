import unittest
from unittest.mock import patch
from src.employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """this basically means that we are working with a class rather than the instance of the class like self"""
        """ runs before anything (in the beginning of the script ) useful if you want to do something once """
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        """runs after everything (in the end of the script ) useful if you want to do something once (maybe its too costly to do before every test )"""
        print("teardownClass")

    def setUp(self):
        """this will run before every single test"""
        # in order to access these from without our other tests use self.
        print("setUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    def tearDown(self):
        """this will run after every single test"""
        print("tearDown\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_repr(self):
        print("test_repr")
        self.assertEqual(
            repr(self.emp_1),
            "Employee('Corey', 'Schafer', 50000, 'Corey.Schafer@email.com')",
        )
        self.assertEqual(
            repr(self.emp_2), "Employee('Sue', 'Smith', 60000, 'Sue.Smith@email.com')"
        )

    def test_str(self):
        print("test_str")
        self.assertEqual(
            str(self.emp_1), "Corey Schafer - $50000 - Corey.Schafer@email.com"
        )
        self.assertEqual(str(self.emp_2), "Sue Smith - $60000 - Sue.Smith@email.com")

    def test_add(self):
        print("test_add")
        total = self.emp_1 + self.emp_2

        self.assertEqual(total, 110000)

    def test_attribute_length(self):
        self.assertEqual(self.emp_1.attribute_length("name"), 5)
        self.assertEqual(self.emp_1.attribute_length("name"), len(self.emp_1.first))
        self.assertEqual(self.emp_2.attribute_length("first"), 3)
        self.assertEqual(self.emp_2.attribute_length("first"), len(self.emp_2.first))

        self.assertEqual(self.emp_1.attribute_length("fullname"), 13)
        self.assertEqual(
            self.emp_1.attribute_length("fullname"), len(self.emp_1.fullname)
        )

        self.assertEqual(self.emp_1.attribute_length("surname"), 7)
        self.assertEqual(self.emp_2.attribute_length("surname"), len(self.emp_2.last))

        self.assertEqual(self.emp_1.attribute_length("last"), 7)
        self.assertEqual(self.emp_1.attribute_length("last"), len(self.emp_1.last))

        self.assertEqual(self.emp_1.attribute_length("email"), len(self.emp_1.email))
        self.assertEqual(
            self.emp_1.attribute_length("email"),
            len(self.emp_1.first) + len(self.emp_1.last) + len(".@gmail.com"),
        )
        self.assertEqual(self.emp_1.attribute_length("email"), 23)

        with self.assertRaises(ValueError):
            self.emp_1.attribute_length("invalid_attribute")

    def test_give_promotion(self):
        self.emp_1.give_promotion(10)
        self.assertEqual(self.emp_1.pay, 55000)

        self.emp_2.give_promotion(20)
        self.assertEqual(self.emp_2.pay, 72000)

        with self.assertRaises(ValueError):
            self.emp_1.give_promotion(-5)

    def test_eq(self):
        self.assertTrue(self.emp_1 == self.emp_1)
        self.assertFalse(self.emp_1 == self.emp_2)

    def test_lt(self):
        self.assertTrue(self.emp_1 < self.emp_2)
        self.assertFalse(self.emp_2 < self.emp_1)
        self.assertFalse(self.emp_1 < self.emp_1)

    def test_monthly_schedule(self):
        """
        We can use patch as a decorator or as a context manager
        This will allow us to mock an object during a test
        and then that object is automatically restored after the test is run.

        In this example I'll use patch as a context manager
        """
        # within patch I pass what I want to mock ( in this case request.get of the employee module )
        with patch("employee.requests.get") as mocked_get:
            # settung the return value of ok to True
            mocked_get.return_value.ok = True
            # setting the return text value
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            # checking to see if the mocked_get was called with the correct url
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")

            # Test a failed response
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
