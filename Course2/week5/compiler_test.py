import unittest
from compiler import LetterCompiler

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)


class TestCompiler(unittest.TestCase):

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    # EDGE CASES HERE
    def test_none(self):
        testcase = "defghingkkdsfs"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
