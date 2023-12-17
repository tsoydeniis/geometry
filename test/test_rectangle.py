import math
import unittest

from rectangle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        arg1 = 0
        arg2 = 12
        res = area(arg1, arg2)
        self.assertEqual(res, 0)
    def test_area_usual(self):
        arg1 = 1000
        arg2 = 777
        res = area(arg1, arg2)
        self.assertEqual(res, arg1 * arg2)
    def test_area_long(self):
        arg1 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        arg2 = 777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        res = area(arg1, arg2)
        self.assertEqual(res, arg1 * arg2)

    def test_area_zero(self):
        arg1 = 0
        arg2 = 0
        res = perimeter(arg1, arg2)
        self.assertEqual(res, 0)

    def test_area_usual(self):
        arg1 = 1000
        arg2 = 777
        res = perimeter(arg1, arg2)
        self.assertEqual(res, 2 * (arg1 + arg2))

    def test_area_long(self):
        arg1 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        arg2 = 777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        res = perimeter(arg1, arg2)
        self.assertEqual(res, 2 * (arg1 + arg2))