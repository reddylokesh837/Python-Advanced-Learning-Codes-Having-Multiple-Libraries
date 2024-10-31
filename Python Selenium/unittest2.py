from math import pi
from unittest1 import circle_area as circle
import unittest


class testArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle(1), pi)
        self.assertAlmostEqual(circle(0),0)
    def testValue(self):
        self.assertRaises(ValueError, circle, -2)
    def testTypes(self):
        self.assertRaises(TypeError,circle,2-2j)
        self.assertRaises(TypeError, circle, True)
        self.assertRaises(TypeError,circle,"radius")

if __name__ == "__main__":
    unittest.main()