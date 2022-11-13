import unittest
from main import*

class My_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2), 4)
    def test_kwargs(self):
        self.assertEqual(adder(12, 25), 37)
    def mised_tests(self):
        self.assertEqual(adder(1, a=2), 3)
    def test_diff(self):
        x = 5
        y = 10
        self.assertEqual(adder(0, 5, x, y), 20)
    def data_type(self):
        self.assertEqual(adder('5','abc', 10), 15)
if __name__ == '__main__':
    unittest.main()