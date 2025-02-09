import math
import unittest


def circumference(radius):
    c = 2 * math.pi * radius
    return round(c, 2)


def area(radius):
    a = math.pi * radius * radius
    return round(a, 2)


class MyTestCase(unittest.TestCase):
    def test_circumference(self):
        tests = [
            # (radius, c)
            (1, 6.28),
            (2, 12.57),
            (3, 18.85),
            (4, 25.13),
            (5, 31.42),
            (6, 37.70),
            (7, 43.98),
            (8, 50.27),
            (9, 56.55),
            (10, 62.83)
        ]
        for radius, expected_c in tests:
            actual_c = circumference(radius)
            self.assertEqual(expected_c, actual_c,
                             f"circumference of a circle with radius={radius} should be {expected_c} but was {actual_c}")

    def test_area(self):
        tests = [
            # (radius, c)
            (1, 3.14),
            (2, 12.57),
            (3, 28.27),
            (4, 50.27),
            (5, 78.54),
            (6, 113.10),
            (7, 153.94),
            (8, 201.06),
            (9, 254.47),
            (10, 314.16)
        ]
        for radius, expected_a in tests:
            actual_a = area(radius)
            self.assertEqual(expected_a, actual_a,
                             f"area of a circle with radius={radius} should be {expected_a} but was {actual_a}")


if __name__ == '__main__':
    unittest.main()
