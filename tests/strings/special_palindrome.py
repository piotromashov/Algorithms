import unittest
from hackerrank.strings.special_palindrome import substrCount

class TestStringsSpecialPalindrome(unittest.TestCase):

    def test_emptyString(self):
        string = ""
        result = substrCount(len(string), string)
        self.assertEqual(result, 0)

    def test_onechar(self):
        string = "a"
        result = substrCount(len(string), string)
        self.assertEqual(result, 1)

    def test_twochars(self):
        string = "aa"
        result = substrCount(len(string), string)
        self.assertEqual(result, 3)

    def test_threechars(self):
        string = "aaa"
        result = substrCount(len(string), string)
        self.assertEqual(result, 6)

    def test_threechars_middledifferent(self):
        string = "aba"
        result = substrCount(len(string), string)
        self.assertEqual(result, 4)

    def test_abcbaba(self):
        string = "abcbaba"
        result = substrCount(len(string), string)
        self.assertEqual(result, 10)

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()