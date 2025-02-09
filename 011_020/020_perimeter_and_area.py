import unittest


def perimeter(a, b):
    return 2 * (a + b)


def area(a, b):
    return a * b


class MyTestCase(unittest.TestCase):
    def test_perimeter(self):
        tests = [
            # ( a, b, perimeter)
            (1, 2, 6),
            (2, 3, 10),
            (3, 4, 14),
            (4, 5, 18),
            (5, 6, 22),
            (6, 7, 26),
            (7, 8, 30),
            (8, 9, 34),
            (9, 10, 38),
            (10, 11, 42)
        ]
        for a, b, expected_p in tests:
            actual_p = perimeter(a, b)
            self.assertEqual(expected_p, actual_p)

    def test_area(self):
        tests = [
            # ( a, b, area)
            (1, 2, 2),
            (2, 3, 6),
            (3, 4, 12),
            (4, 5, 20),
            (5, 6, 30),
            (6, 7, 42),
            (7, 8, 56),
            (8, 9, 72),
            (9, 10, 90),
            (10, 11, 110)
        ]
        for a, b, expected_a in tests:
            actual_a = area(a, b)
            self.assertEqual(expected_a, actual_a)


if __name__ == '__main__':
    unittest.main()
