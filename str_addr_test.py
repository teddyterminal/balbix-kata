import unittest
import sys
from unittest.mock import patch
from str_adder import add
import str_adder

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

    def test_multiple_delimiters(self):
        self.assertEqual(add("//[!][:]\n3!4:5!6"), 18)

    def test_even_more_delimiters(self):
        self.assertEqual(add("//[~][!][#][^][?][+]\n3~4!5#6#7^8?9+1+2"), 45)

    def test_long_length_multiple_delimiters(self):
        self.assertEqual(add("//[***][2.71828182][?!?]\n3?!?4?!?52.718281826***7***8"), 33)

    @patch("str_adder.print")
    def test_prints_output(self, mock_print):
        self.assertEqual(add("4, 5, 6"), 15)
        mock_print.assert_called_with(15)

    @patch("str_adder.print")
    def test_prints_output_more_delimiters(self, mock_print):
        self.assertEqual(add("//[***][?!?]\n4***5, 6?!?7"), 22)
        mock_print.assert_called_with(22)

    @patch("str_adder.print")
    def test_command_line_input(self, mock_print):
        sys.argv = ["str_adder.py", "scalc", "1, 2, 3"]
        str_adder.main()
        mock_print.assert_called_with("The result is 6")

if __name__ == '__main__':
    unittest.main()
