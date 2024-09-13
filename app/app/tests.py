from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 4)

        self.assertEqual(res, 6)

    def test_double(self):
        res = calc.double(5)

        self.assertEqual(res, 10)
