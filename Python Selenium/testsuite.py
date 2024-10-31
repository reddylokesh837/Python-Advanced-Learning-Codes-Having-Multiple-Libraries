"""
In most cases, calling unittest.main() will collect all the module’s test cases  and executes them.

However, It is suggested to use TestCase implementations to group tests together according to the features they test. unittest provides a mechanism for this, the test suite, represented by unittest’s TestSuite class."""



from math import pi
import unittest


object1= None

class Circle():
    def circle_area(self,radius):
        if type(radius) not in [int, float]:
            #throws an error if the radius is not of type int/float
            raise TypeError("The radius must be a non-negative real number")
       
        if radius < 0:
            #throws an error , if radius is a negative value
            raise ValueError("The radius cannot be negative.")
        return pi * (radius ** 2)


def setUpModule():
    object1 = Circle()
    print("Im the setUpModule")
    return object1


def tearDownModule():
    global object1
    object1= None
    print("Im the tearDownModule")


class TestCircle(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.a =[2,3,10]

    @classmethod
    def tearDownClass(cls) -> None:
        print("Im the teardown class")


    def setUp(self) -> None:
        print("before tests method")

    def tearDown(self) -> None:
        print("after the tests methods")
    
    def test_1(self):
        print("Im the test 1")
        print(setUpModule().circle_area(self.a[0]))
    
    def test_2(self):
        print("Im the test 2")
        print(setUpModule().circle_area(self.a[1]))
    
    def test_3(self):
        print("Im the test 3")
        print(setUpModule().circle_area(self.a[2]))


# instead of using unittest.main()
# if __name__ == "__main__":
#     unittest.main()


# use TestSuite()
if __name__ == "__main__":
    tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCircle)
    test_suite = unittest.TestSuite([tc1])

    unittest.TextTestRunner(verbosity=1).run(test_suite)
