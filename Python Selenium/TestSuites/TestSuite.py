import unittest
from TestCases_PackGo.BaseClass import BaseClass
from TestCases_PackGo.TestCase1 import Login 
from TestCases_PackGo.TestCase2 import SignUp

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    #get all tests from Login and SignUp class
    tc1=unittest.TestLoader().loadTestsFromTestCase(Login)
    tc2=unittest.TestLoader().loadTestsFromTestCase(SignUp)
    # create a test suite combining tc1 and tc2
    test_suite = unittest.TestSuite([tc1,tc2]) 
    # run the suite
    unittest.TextTestRunner(verbosity=1).run(test_suite)

