"""
setUp() in unittest
The setUp() method is a special method in the unittest framework that is called before each test method in your test case class. Its primary purpose is to prepare the test environment, ensuring that each test starts with a known state.

Key Points about setUp()
Execution Order: setUp() is called immediately before each test method (i.e., any method that begins with test_).

Exception Handling: If setUp() raises an exception:

The test framework considers the test as having encountered an error.
None of the test methods in that test case will be executed.
The tearDown() method will also be skipped for that test case.
Common Use Cases:

Initializing objects that are used across multiple test methods.
Setting up test databases or files.
Creating mock objects or stubs.
Isolation: Each test method starts with a clean state due to the fresh call to setUp(), which enhances test isolation.
"""

import unittest


class TestCaseCreation(unittest.TestCase):
    def setUp(self):
        print("Setup method")

    def test_A(self):
        print("Im the test one")
        raise Exception("Stop execution of test one")


    def test_B(self):
        print("Im the test two")

    def test_C(self):
        print("Im the test 3")

    def tearDown(self):
        print("Im the tear down method \n")


if __name__=="__main__":
    unittest.main()
