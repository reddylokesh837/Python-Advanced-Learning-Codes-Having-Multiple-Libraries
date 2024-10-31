import unittest
from math import pi


class Circle:
    def circle_area(self,radius):
        if type(radius) not in [int, float]:
            raise TypeError("The radius should be in int/float")
        if radius<0:
            raise ValueError("The radius should not be negative")
        return pi *(radius**2)
    
#object1 is declared as a global variable at the top of the file. This allows it to be accessible in both setUpModule() and the test methods.
object1= None

def setUpModule():
    global object1
    object1 = Circle()
    print("Im the setUpModule")
    return object1

def tearDownModule():
    global object1
    object1= None
    print("Im the tearDownModule")

class test_circle(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Im the setup class method")
        cls.a = [1,0,-2,3+4j,True,"radius"]

    @classmethod
    def tearDownClass(cls) -> None:
        print("Im the teardown class method")


    def setUp(self) -> None:
        print("before tests method")

    def tearDown(self) -> None:
        print("after the tests method \n")


    def test_A(self):
        self.assertAlmostEqual(setUpModule().circle_area(self.a[0]), pi)

    def test_B(self):
        self.assertRaises(ValueError, object1.circle_area , self.a[2])
        
    def test_C(self):
        self.assertRaises(TypeError, object1.circle_area, self.a[3])

if __name__ == "__main__":
    unittest.main()