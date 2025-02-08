import unittest


def find_max(numbers):
    max_number = numbers[0]
    for n in numbers:
        if n > max_number:
            max_number = n
    return max_number


class MyTestCase(unittest.TestCase):
    def test_find_max(self):
        tests = [
            # (numbers, max_number)
            ([0], 0),
            ([1, 3, 9], 9),
            ([100, 10, 101], 101),
            ([10, 10, 10], 10),
            ([5, 2, 1, 4, 3], 5)
        ]

        for numbers, expected_max_number in tests:
            actual_max_number = find_max(numbers)
            self.assertEqual(expected_max_number, actual_max_number)


if __name__ == '__main__':
    unittest.main()
