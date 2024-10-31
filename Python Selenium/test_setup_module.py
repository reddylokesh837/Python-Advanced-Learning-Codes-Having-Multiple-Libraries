import unittest



"""
You might use setUpModule() for setting up a database connection or test environment that will be shared across different classes or tests.
tearDownModule() could be used to clean up global resources like shutting down external services after all tests in the module are done.

"""
def setUpModule():
    print("Im setup module")

def tearDownModule():
    print("Im the tear down module")

class TestCaseCreation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Im the setup class")
    
    @classmethod
    def tearDownClass(cls) -> None:
        print("Im the class tear down method")

    def setUp(self) -> None:
        print("Im the setup method")
    
    def tearDown(self) -> None:
        print("Im the tear down method")

    def test_A(self):
        print("Im the test one")
    
    def test_B(self):
        print("Im the test two")


if __name__=="__main__":
    unittest.main()