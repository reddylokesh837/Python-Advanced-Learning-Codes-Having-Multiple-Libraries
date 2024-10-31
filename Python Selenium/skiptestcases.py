
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


class test_circle(unittest.TestCase):
    circleObject = None
    radius =2


    @classmethod
    def setUpClass(cls) -> None:
        cls.circleObject = Circle()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.circleObject = None

    def test_area(self):
        self.assertAlmostEqual(self.circleObject.circle_area(1), pi)
        self.assertAlmostEqual(self.circleObject.circle_area(0),0)
    
    @unittest.skipIf(radius<0, "negative value")
    def test_value(self):
        Circle().circle_area(-2)
    

    @unittest.skipUnless(type(radius) in [int, float], "Non-numeric value")
    @unittest.expectedFailure
    def test_types(self):
        self.circleObject.circle_area(2-3j)

    

if __name__ == "__main__":
    unittest.main()