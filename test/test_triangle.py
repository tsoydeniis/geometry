import math
import unittest

from triangle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        arg1 = 10
        arg2 = 0
        res = area(arg1, arg2)
        self.assertEqual(res, 0)
    def test_area_usual(self):
        arg1 = 1000
        arg2 = 18
        res = area(arg1, arg2)
        self.assertEqual(res, arg1 * arg2 / 2)
    def test_area_long(self):
        arg1 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        arg2 = 9999999999
        res = area(arg1, arg2)
        self.assertEqual(res, arg1 * arg2 / 2)

    def test_area_zero(self):
        arg1 = 0
        arg2 = 0
        arg3 = 0
        res = perimeter(arg1, arg2, arg3)
        self.assertEqual(res, 0)

    def test_area_usual(self):
        arg1 = 1000
        arg2 = 777
        arg3 = 666
        res = perimeter(arg1, arg2, arg3)
        self.assertEqual(res, arg1 + arg2 + arg3)

    def test_area_long(self):
        arg1 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        arg2 = 99999999999999999999999999999999999999999
        arg3 = 9999999999999999
        res = perimeter(arg1, arg2, arg3)
        self.assertEqual(res, arg1 + arg2 + arg3)