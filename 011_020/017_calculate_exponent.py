import unittest


def power(a, n):
    result = 1
    for _ in range(0, n):
        result = result * a
    return result


class MyTestCase(unittest.TestCase):
    def test_power(self):
        tests = [
            # (a, n, a^n)
            (2, 0, 1),
            (3, 3, 27),
            (10, 5, 100000),
        ]

        for a, n, expected in tests:
            actual = power(a, n)
            self.assertEqual(expected, actual, f"{a}^{n} should be {expected} but was {actual}")


if __name__ == '__main__':
    unittest.main()
