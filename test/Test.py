import unittest

def double(a):
    return a * 2

class TestMyFunctions(unittest.TestCase):
    """
    Testing Unit Tests in Python.
    """

    def test_double(self):
        """
        Test if double(a) function really doubles the value given.
        """

        self.assertEqual(double(3), 6)
        self.assertEqual(double(4), 8)
        self.assertTrue(True);

if __name__ == '__main__':
    unittest.main()