import unittest
from str_adder import add

class TestStringAdder(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(add(""), 0)

    def test_one_number(self):
        self.assertEqual(add("2"), 2)

    def test_one_negative_number(self):
        self.assertEqual(add("-1"), -1)

    def test_two_numbers(self):
        self.assertEqual(add("5,7"), 12)

    def test_two_numbers_onepos_oneneg(self):
        self.assertEqual(add("-3, 5"), 2)

    def test_two_numbers_bothneg(self):
        self.assertEqual(add("-3,-3"), -6)

if __name__ == '__main__':
    unittest.main()
