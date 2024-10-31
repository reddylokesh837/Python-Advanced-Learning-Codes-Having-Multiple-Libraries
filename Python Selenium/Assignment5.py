from pdb import run
import unittest
from math import pi


class Calculator(object):
    def add(self, x, y):
        return x+y
    def sub(self, x, y):
        return x-y
    def multiply(self, x, y):
        return x * y
    def divide(self, x,y):
        return x/y
    

object1 = None

def setUpModule():
    global object1
    print("Im the setup module")
    object1 =  Calculator()
    return object1

def tearDownModule():
    print("Im the teardown module")
    object1 = None


class Test_Calculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Im the class method")
        cls.a = 10
        cls.b = 5
    
    @classmethod
    def tearDownClass(cls) -> None:
        print("Im the tear down method")


    def setUp(self) -> None:
        print("Im setup method")

    def tearDown(self) -> None:
        print("Im teardown method\n")


    def test_1(self):
        self.assertAlmostEqual(object1.add(self.a, self.b), 15) 

    def test_2(self):
        self.assertAlmostEqual(object1.sub(self.a, self.b), 5)
    
    def test_3(self):
        self.assertAlmostEqual(object1.multiply(self.a, self.b), 50)
    
    def test_4(self):
        self.assertAlmostEqual(object1.divide(self.a, self.b), 2)

    @unittest.skipUnless(lambda self: isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)), "Skipping because values are not valid")
    def test_5(self):
        self.assertAlmostEqual(object1.divide(self.a, self.b), 2)
    
    @unittest.skipUnless(lambda self: self.a >= 0 and self.b >= 0, "Skipping because values are negative")
    def test_non_negative_add(self):
        self.assertAlmostEqual(object1.add(self.a, self.b), 15)

    @unittest.skipUnless(lambda self: self.a >= 0 and self.b >= 0, "Skipping because values are negative")
    def test_non_negative_multiply(self):
        self.assertAlmostEqual(object1.multiply(self.a, self.b), 50)





if __name__ == "__main__":
    tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_Calculator)

    test_suite = unittest.TestSuite([tc1])
    unittest.TextTestRunner(verbosity=1).run(test_suite)

    