import unittest
from math import pi



class Calculator:
    def add(self, x,y):
        return x+y
    def sub(self, x,y):
        return x-y
    
    def multiply(self, x, y):
        return x*y
    
    def divide(self, x, y):
        return x/y
    


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        print("Im setup method")
        self.calc = Calculator()

    
    def tearDown(self) -> None:
        print("Im teardown method\n")

    def test_1(self):
        self.assertAlmostEqual(self.calc.add(10,3),13)
        self.assertAlmostEqual(self.calc.add(20,30), 50)
        self.assertAlmostEqual(self.calc.add(10,30),40)
        self.assertAlmostEqual(self.calc.add(10,10),20)

    def test_2(self):
        self.assertAlmostEqual(self.calc.sub(10,3),7)
        self.assertAlmostEqual(self.calc.sub(100,50), 50)
        self.assertAlmostEqual(self.calc.sub(10,30),-20)
        self.assertAlmostEqual(self.calc.sub(10,10),0)
        
    def test_3(self):
        self.assertAlmostEqual(self.calc.multiply(10,3),30)
        self.assertAlmostEqual(self.calc.multiply(10,10), 100)
        self.assertAlmostEqual(self.calc.multiply(10,30),300)
        self.assertAlmostEqual(self.calc.multiply(10,10),100)
    
    def test_4(self):
        self.assertAlmostEqual(self.calc.divide(10,3),3.3333333333333335)
        self.assertAlmostEqual(self.calc.divide(100,50), 2)
        self.assertAlmostEqual(self.calc.divide(10,30),0.3333333333333333)
        self.assertAlmostEqual(self.calc.divide(10,10),1)



if __name__ == "__main__":
    tc1 =  unittest.TestLoader().loadTestsFromTestCase(TestCalculator)

    test_suite = unittest.TestSuite([tc1])

    unittest.TextTestRunner(verbosity=1).run(test_suite)

    