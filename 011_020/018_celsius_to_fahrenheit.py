import unittest


def c_to_f(c):
    return (c * 9 / 5) + 32


class MyTestCase(unittest.TestCase):
    def test_c_to_f(self):
        tests = [
            # (c, f)
            (0, 32),
            (10, 50),
            (20, 68),
            (30, 86),
            (40, 104),
            (50, 122),
            (60, 140),
            (70, 158),
            (80, 176),
            (90, 194),
            (0.5, 32.9),
            (1.5, 34.7),
            (2.5, 36.5),
            (3.5, 38.3),
            (4.5, 40.1),
            (5.5, 41.9),
            (6.5, 43.7),
            (7.5, 45.5),
            (8.5, 47.3),
            (9.5, 49.1),
            (-1, 30.2),
            (-5, 23),
            (-10, 14),
            (-15, 5),
            (-20, -4),
            (-25, -13),
            (-30, -22),
            (-35, -31),
            (-40, -40),
            (-45, -49),
        ]
        for c, expected_f in tests:
            actual_f = c_to_f(c)
            self.assertEqual(expected_f, actual_f,
                             f"[{c}C should equal to {expected_f}F but got {actual_f}F")


if __name__ == '__main__':
    unittest.main()
