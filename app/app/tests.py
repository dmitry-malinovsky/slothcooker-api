from django.test import TestCase
from app.calc import sum

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Two numbers are summed properly"""
        self.assertEqual(sum(3, 8), 11)
