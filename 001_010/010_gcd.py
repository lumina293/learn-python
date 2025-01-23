import unittest


# function under test
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class MyTestCase(unittest.TestCase):
    # test function
    def test_gcd(self):
        # test data, or test cases
        tests = [
            (20, 20, 20),
            (10, 30, 10),
            (30, 10, 10),
            (4, 5, 1),
            (6, 8, 2),
            (10, 5, 5),
            (20, 0, 20),
            (0, 20, 20)
        ]

        for a, b, expected_gcd in tests:
            actual_gcd = gcd(a, b)
            self.assertEqual(expected_gcd, actual_gcd, f"gcd({a}, {b}) should be {expected_gcd} but got {actual_gcd}")


if __name__ == '__main__':
    unittest.main()
