import unittest
from str_adder import add

class TestStringAdder(unittest.TestCase):

    def test_empty_equals_zero(self):
        self.assertEqual(add(""), 0)

    def test_one_number(self):
        self.assertEqual(add("2"), 2)

    def test_two_numbers(self):
        self.assertEqual(add("5,7"), 12)

    def test_many_numbers(self):
        self.assertEqual(add("4,5,6"), 15)

    def test_many_numbers_2(self):
        self.assertEqual(add("0,1,2,6"), 9)

    def test_newline_separator_sum(self):
        self.assertEqual(add("0\n1\n2"), 3)

    def test_newline_and_commas_separator(self):
        self.assertEqual(add("0,1\n6\n4,5"), 16)

    def test_new_delimiter(self):
        self.assertEqual(add("//;\n0;1;4"), 5)

    def test_no_negatives_allowed(self):
        self.assertRaises(Exception, add, "-3, -5")

    def test_negative_exception_message(self):
        try:
            add("-3, -5")
            self.assertFail()
        except Exception as e:
            self.assertEqual(str(e), "negatives not allowed: (-3, -5)")

    def test_ignore_greater_than_1000(self):
        self.assertEqual(add("3, 1001"), 3)

    def test_multiple_greater_than_1000(self):
        self.assertEqual(add("1001, 1002, 213485"), 0)

    def test_1000_borderline_not_ignored(self):
        self.assertEqual(add("1000, 1000, 18"), 2018)

    def test_longer_length_delimiter(self):
        self.assertEqual(add("//[***]\n3***4***5"), 12)

    def test_even_longer_length_delimiter(self):
        self.assertEqual(add("//[3.1415926]\n33.141592643.14159265"), 12)




if __name__ == '__main__':
    unittest.main()
