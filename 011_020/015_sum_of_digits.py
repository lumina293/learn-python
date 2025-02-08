import unittest


def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        last_digit = n % 10
        total = total + last_digit
        n = n // 10
    return total


class MyTestCase(unittest.TestCase):
    def test_sum_of_digits(self):
        tests = [
            # (n, total)
            (0, 0),
            (123, 6),
            (1610, 8),
            (204, 6),
            (-1345, 13),
            (101010, 3)
        ]
        for n, expect_total in tests:
            actual_total = sum_of_digits(n)
            self.assertEqual(expect_total, actual_total)  # add assertion here


if __name__ == '__main__':
    unittest.main()
