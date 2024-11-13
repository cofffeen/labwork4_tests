import unittest

def area(a):
    # принимает число a, возвращает площадь квадрата со стороной a
    return a * a


def perimeter(a):
    # принимает число a, возвращает периметр квадрата со стороной a
    return 4 * a

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


    def test_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()
