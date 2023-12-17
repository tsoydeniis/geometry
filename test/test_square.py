import math
import unittest

from square import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        arg1 = 0
        res = area(arg1)
        self.assertEqual(res, 0)
    def test_area_usual(self):
        arg1 = 1000
        res = area(arg1)
        self.assertEqual(res, arg1 * arg1)
    def test_area_long(self):
        arg1 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        res = area(arg1)
        self.assertEqual(res, arg1 * arg1)

    def test_area_zero(self):
        arg1 = 0
        res = perimeter(arg1)
        self.assertEqual(res, 0)

    def test_area_usual(self):
        arg1 = 1000
        res = perimeter(arg1)
        self.assertEqual(res,4 * arg1)

    def test_area_long(self):
        arg1 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        res = perimeter(arg1)
        self.assertEqual(res, 4 * arg1)