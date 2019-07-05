from django.test import TestCase

from app.calc import sum, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Two numbers are summed properly"""
        self.assertEqual(sum(3, 8), 11)

    def test_subtract_test(self):
        """Two numbers are subtracted properly"""
        self.assertEqual(subtract(10,5),5)
