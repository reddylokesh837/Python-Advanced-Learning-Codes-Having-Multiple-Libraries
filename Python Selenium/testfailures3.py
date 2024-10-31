import unittest
from math import pi


class Circle():
    def circle_area(self,radius):
        if type(radius) not in [int, float]:
            #throws an error if the radius is not of type int/float
            raise TypeError("The radius must be a non-negative real number")
       
        if radius < 0:
            #throws an error , if radius is a negative value
            raise ValueError("The radius cannot be negative.")
        return pi * (radius ** 2)

class testArea(unittest.TestCase):
    def test_area(self):
        cObject = Circle()
        self.assertAlmostEqual(cObject.circle_area(1),pi)
    
    # expected failure scenarios
    @unittest.expectedFailure
    def testValue(self):

        cObject = Circle()
        cObject.circle_area(-2)
    
    def testTypes(self):
        cObject =Circle()
        self.assertRaises(TypeError, cObject.circle_area, 3-2j)
        self.assertRaises(TypeError, cObject.circle_area, True)
        self.assertRaises(TypeError, cObject.circle_area,"radius")


if __name__ == "__main__":
    unittest.main()