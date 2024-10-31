import unittest
from math import pi


class Circle:
    def circle_area(self,radius):
        if type(radius) not in [int, float]:
            raise TypeError("The radius should be in int/float")
        if radius<0:
            raise ValueError("The radius should not be negative")
        return pi *(radius**2)
    


class test_circle(unittest.TestCase):
    def testarea(self):
        cObject = Circle()
        self.assertAlmostEqual(cObject.circle_area(1), pi)

    
    def testValue(self):
        cObject = Circle()
        cObject.circle_area(-2)

    def testTypes(self):
        cObject = Circle()
        self.assertRaises(TypeError,cObject.circle_area, "radius")
        self.assertRaises(TypeError, cObject.circle_area, 2-4j)
        self.assertRaises(TypeError, cObject.circle_area,True)
        self.assertRaises(ValueError, cObject.circle_area,-2)


if __name__ =="__main__":
    unittest.main()