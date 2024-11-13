import math

import unittest

def area(r):
    # принимает число r, возвращает площадь окружности радиусом r
    return math.pi * r * r


def perimeter(r):
    # принимает число r, возвращает периметр окружности радиусом r
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(2)
        self.assertEqual(res, 12.566370614359172)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 12.566370614359172)

if __name__ == '__main__':
    unittest.main()
