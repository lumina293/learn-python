import unittest
import math


def solve_quadratic(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return []
    if delta == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return [x1, x2]


class MyTestCase(unittest.TestCase):
    def test_solve_quadratic(self):
        tests = [
            # ([a, b, c], [x1, x2])
            ([3, 2, 4], []),
            ([1, -49, -50], [-1, 50]),
            ([2, -7, 3], [3, 1 / 2]),
            ([1, 2, 1], [-1])
        ]
        for [a, b, c], expected in tests:
            actual = solve_quadratic(a, b, c)
            self.assertCountEqual(expected, actual,
                                  f"quadratics of {a, b, c} should be {expected} but got {actual}")  # add assertion here


if __name__ == '__main__':
    unittest.main()
