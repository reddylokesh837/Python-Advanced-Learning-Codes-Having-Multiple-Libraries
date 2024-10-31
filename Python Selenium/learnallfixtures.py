import unittest
from math import pi


class Circle:
    def circle_area(self,radius):
        if radius < 0:
            raise ValueError("The raidus should not be a negative!")
        if type(radius) not in [int, float]:
            raise TypeError("The radius should be int/float only")
        return pi *(radius**2)
    

object1 = None

def setUpModule():
    object1 = Circle()
    print("Im the setup module")
    return object1

def tearDownModule():
    object1= None


class test_area(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Im the setup class method")
        cls.a=[2,3,10,1]
    

    @classmethod
    def tearDownClass(cls):
        print("Im the teardown class")

    
    def setUp(self) -> None:
        print("before tests method")

    def tearDown(self) -> None:
        print("after the tests method \n")

    
    def test1(self):
        print("Im the test one")
        print(setUpModule().circle_area(self.a[0]))

    def test2(self):
        print("Im the test two")
        print(setUpModule().circle_area(self.a[1]))
        self.assertAlmostEqual(setUpModule().circle_area(self.a[3]), pi)
    
    def test3(self):
        print("Im the test three")
        print(setUpModule().circle_area(self.a[2]))


if __name__== "__main__":
    unittest.main()