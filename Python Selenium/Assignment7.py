import unittest
from math import pi



class Calulator:
    def add(self, x,y):
        return x+y
    def sub(self, x,y):
        return x-y
    def multiply(self, x, y):
        return x*y

    def divide(self, x, y):
        return x/y
    

def setUpModule():
    print("Im the setup module")
    global object1
    object1 = Calulator()
    return object1

def tearDownModule():
    print("Im the teardown module")
    global object1
    object1 = None


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Im the class method")
        cls.test_data = [(10,3),(20,30),(10,30),(10,10)]

    @classmethod
    def tearDownClass(cls):
        print("Im the teardown class")

    def setUp(self):
        print("Im setup method")
    
    def tearDown(self):
        print("Test completed\n")


    def test_A(self):
        for x, y in self.test_data:
            self.assertAlmostEqual(object1.add(x,y), x+y)

        
    def test_B(self):
        for x,y in self.test_data:
            self.assertAlmostEqual(object1.sub(x,y),x-y)

    def test_C(self):
        for x,y in self.test_data:
            self.assertAlmostEqual(object1.multiply(x,y), x*y)

    def test_D(self):
        for x,y in self.test_data:
            self.assertAlmostEqual(object1.divide(x,y),x/y)

        
    
if __name__ =="__main__":
    tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    test_suite= unittest.TestSuite([tc1])

    unittest.TextTestRunner(verbosity=1).run(test_suite)