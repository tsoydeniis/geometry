import math
import unittest

from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        arg = 0
        res = area(arg)
        self.assertEqual(res, arg)
    def test_area_usual(self):
        arg = 1000
        res = area(arg)
        self.assertEqual(res, arg * arg * math.pi)
    def test_area_long(self):
        arg = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        res = area(arg)
        self.assertEqual(res, arg * arg * math.pi)

    def test_perimeter_zero(self):
        arg = 0
        res = perimeter(arg)
        self.assertEqual(res, arg)
    def test_perimeter_usual(self):
        arg = 1000
        res = perimeter(arg)
        self.assertEqual(res, arg * 2 * math.pi)
    def test_perimeter_long(self):
        arg = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        res = perimeter(arg)
        self.assertEqual(res, arg * 2 * math.pi)