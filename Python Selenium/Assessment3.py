import unittest
from Assessment1 import Login
from Assessment2 import AddCustomer


if __name__ == "__main__":
    tc1 = unittest.TestLoader().loadTestsFromTestCase(Login)
    tc2 = unittest.TestLoader().loadTestsFromTestCase(AddCustomer)
    test_suite = unittest.TestSuite([tc1,tc2])
    unittest.TextTestRunner(verbosity=1).run(test_suite)