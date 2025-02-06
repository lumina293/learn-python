import unittest


def calculate_sum(n):
    result = (n * (n + 1)) / 2
    return result


class MyTestCase(unittest.TestCase):
    def test_calculate_sum(self):
        tests = [
            # (n, 1+2+...+n)
            (0, 0),
            (1, 1),
            (2, 3),
            (3, 6),
            (9, 45)
        ]
        for n, expected_sum in tests:
            actual_sum = calculate_sum(n)
            self.assertEqual(expected_sum, actual_sum, f"sum(1..{n}) should be {expected_sum} but got {actual_sum}")
