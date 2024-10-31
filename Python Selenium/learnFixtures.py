from turtle import circle
import unittest
from math import pi


class Circle:
    """self: This refers to the instance of the class on which the method is called. By adding self as the first parameter, you're telling Python that circle_area() should work on an instance of the Circle class."""
    def circle_area(self,radius):
        if radius <0:
            raise ValueError("The radius cannot be negative!")
        if type(radius) not in [int, float]:
            raise TypeError("The radius should not be a string")
        return pi *(radius**2)
    

class test_circle(unittest.TestCase):
    def testArea(self):
        pass


class testarea_circle(unittest.TestCase):
    def test_A(self):
        cObject = Circle()
        self.assertAlmostEqual(cObject.circle_area(1), pi)
    
    def test_B(self):
        cObject = Circle()
        self.assertAlmostEqual(cObject.circle_area(0),0)
        self.assertRaises(TypeError,cObject.circle_area, "radius")
        self.assertRaises(ValueError, cObject.circle_area,-2)
        self.assertRaises(TypeError, cObject.circle_area, 2-4j)


if __name__ == "__main__":
    unittest.main()