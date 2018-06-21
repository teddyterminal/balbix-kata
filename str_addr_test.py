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

    def test_many_numbers(self):
        self.assertEqual(add("4,5,6,-4"), 11)

    def test_many_numbers_2(self):
        self.assertEqual(add("0,1,2,6"), 9)

    def test_newline(self):
        self.assertEqual(add("0\n1\n2"), 3)

    def test_newline_commas(self):
        self.assertEqual(add("0,1\n6\n-4,-5"), -2)

if __name__ == '__main__':
    unittest.main()
