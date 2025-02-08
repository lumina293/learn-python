import unittest


def is_palindrome(s):
    s = s.lower()
    for i in range(0, len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_is_palindrome(self):
        tests = [
            # (s, is_palindrome)
            ("123", False),
            ("d23r32d", True),
            ("1s2ee2s1", True),
            ("4r123324r4", False),
            ("abcaba", False),
            ("Madam", True)
        ]

        for s, expected in tests:
            actual = is_palindrome(s)
            self.assertEqual(expected, actual, f"is {s} palindrome?")


if __name__ == '__main__':
    unittest.main()
