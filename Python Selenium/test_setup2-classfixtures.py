import unittest

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

# Test Case for the Counter class
# tests naming convention should be in ascending order of the alphabets then it will run in that order otherwise order of execution will get wrong executions
class TestCounter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up the counter for all tests...")
        cls.counter = Counter()  # Initialize the counter once for all tests

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the counter after all tests...")
        cls.counter.reset()  # Reset the counter after all tests

    def test_A(self):
        self.counter.increment()
        self.assertEqual(self.counter.value, 1)  # Should be 1 after one increment

    def test_B(self):
        self.counter.increment()
        self.counter.increment()
        self.assertEqual(self.counter.value, 3)  # Should be 3 after two increments

    def test_C(self):
        self.counter.increment()
        self.counter.increment()
        self.counter.increment()
        self.assertEqual(self.counter.value, 6)  # Should be 6 after three increments

# Run the tests
if __name__ == '__main__':
    unittest.main()
