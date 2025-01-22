import unittest
from src.colors import Color, color_to_hex


class TestColorEnum(unittest.TestCase):

    def test_enum_values(self):
        # Test that the enum members have correct values
        self.assertEqual(Color.RED.value, 1)
        self.assertEqual(Color.GREEN.value, 2)
        self.assertEqual(Color.BLUE.value, 3)

    def test_enum_names(self):
        # Test that the enum members have correct names
        self.assertEqual(Color.RED.name, "RED")
        self.assertEqual(Color.GREEN.name, "GREEN")
        self.assertEqual(Color.BLUE.name, "BLUE")

    def test_enum_equality(self):
        # Test that the equality operator works as expected
        self.assertTrue(Color.RED == Color.RED)
        self.assertFalse(Color.RED == Color.GREEN)
        self.assertTrue(Color.RED == Color(1))  # Test with value

    # def test_color_to_hex(self):
    #     # Test that the color_to_hex function returns the correct hex codes
    #     self.assertEqual(color_to_hex(Color.RED), "#FF0000")
    #     self.assertEqual(color_to_hex(Color.GREEN), "#00FF00")
    #     self.assertEqual(color_to_hex(Color.BLUE), "#0000FF")
    #     self.assertEqual(
    #         color_to_hex(Color(999)), "Unknown color"
    #     )  # Test for unknown color

    def test_describe_method(self):
        # Test that the describe method returns the correct descriptions
        self.assertEqual(Color.RED.describe(), "The color of passion and energy.")
        self.assertEqual(Color.GREEN.describe(), "The color of nature and tranquility.")
        self.assertEqual(Color.BLUE.describe(), "The color of calm and stability.")

    # def test_iterate_over_colors(self):
    #     # Test that iterating over colors gives the correct output
    #     colors = list(Color)
    #     self.assertEqual([color.name for color in colors], ["RED", "GREEN", "BLUE"])
    #     self.assertEqual([color.value for color in colors], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
