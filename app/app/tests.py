from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):
    """Class that holds tests"""

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(8, 3), 11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted"""
        self. assertEquals(subtract(8, 4), 3)
