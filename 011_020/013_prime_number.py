import unittest


def is_prime_number(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for d in range(5, int(n ** 0.5) + 1, 2):
        if n % d == 0:
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_is_prime_number(self):
        tests = [
            # (n, is prime?)
            (0, False),
            (1, False),
            (2, True),
            (4, False),
            (7, True),
            (10, False),
            (11, True)
        ]

        for n, expected_prime in tests:
            actual_prime = is_prime_number(n)
            print(f"{n} is prime number should be {expected_prime} and actual is: {actual_prime}")

            self.assertEqual(expected_prime, actual_prime,
                             f"{n} is prime number should be {expected_prime} but got {actual_prime}")


if __name__ == '__main__':
    unittest.main()
