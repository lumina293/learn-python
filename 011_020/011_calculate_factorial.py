import unittest


def factorial(n):
    result = 1
    for a in range(1, n + 1):
        result = result * a
    return result


def factorial2(n):
    if n == 0:
        return 1
    return n * factorial2(n - 1)


class MyTestCase(unittest.TestCase):
    # test function
    def test_factorial(self):
        # test data, or test cases
        tests = [
            # (n, n!)
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (7, 5040),
            (10, 3628800)
        ]

        for n, expected_factorial in tests:
            actual_factorial = factorial(n)
            self.assertEqual(expected_factorial, actual_factorial,
                             f"{n}! should be {expected_factorial} but got {actual_factorial}")

    def test_factorial2(self):
        tests = [
            (5, 120),
            (6, 720),
            (8, 5040 * 8),
            (9, 362880)
        ]
        for n, expected in tests:
            actual = factorial2(n)
            self.assertEqual(expected, actual, f"{n}! should be {expected} but got {actual}")


if __name__ == '__main__':
    unittest.main()
