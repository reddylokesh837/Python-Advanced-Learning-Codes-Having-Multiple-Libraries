import unittest


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_count(self):
        return self.count


class TestCounter(unittest.TestCase):
    def setUp(self):
        self.counter = Counter()  # Fresh instance before each test

    def test_increment(self):
        self.counter.increment()
        self.assertEqual(self.counter.get_count(), 1)  # Check if increment works

    def test_decrement(self):
        self.counter.decrement()
        self.assertEqual(self.counter.get_count(), -1)  # Check if decrement works

    def test_multiple_operations(self):
        self.counter.increment()
        self.counter.increment()
        self.counter.decrement()
        self.assertEqual(self.counter.get_count(), 1)  # Check final count

# Run the tests
if __name__ == '__main__':
    unittest.main()
