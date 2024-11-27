import unittest

import circle
import rectangle
import triangle
import square

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = circle.area(2)
        self.assertEqual(res, 12.566370614359172)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = circle.perimeter(2)
        self.assertEqual(res, 12.566370614359172)

    def test_wrong_perimeter(self):
        res = circle.perimeter(-2)
        self.assertEqual(res, 0)
    
    def test_wrong_area(self):
        res = circle.area(-2)
        self.assertEqual(res, 0)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(0, 10)
        self.assertEqual(res, 0)

    def test_area(self):
        res = rectangle.area(1, 2)
        self.assertEqual(res, 2)
    
    def test_wrong_area(self):
        res = rectangle.area(1, -2)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = rectangle.perimeter(1, 2)
        self.assertEqual(res, 6)
    
    def test_wrong_perimeter(self):
        res = rectangle.perimeter(1, -2)
        self.assertEqual(res, 0)

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = square.area(2)
        self.assertEqual(res, 4)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)


    def test_perimeter(self):
        res = square.perimeter(2)
        self.assertEqual(res, 8)

    def test_wrong_perimeter(self):
        res = square.perimeter(-2)
        self.assertEqual(res, 0)
    
    def test_wrong_area(self):
        res = square.area(-2)
        self.assertEqual(res, 0)

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0, 10)
        self.assertEqual(res, 0)

    def test_area(self):
        res = triangle.area(1, 2)
        self.assertEqual(res, 1)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)


    def test_perimeter(self):
        res = triangle.perimeter(1, 2, 2)
        self.assertEqual(res, 5)

    def test_wrong_perimeter(self):
        res = triangle.perimeter(-1, -2, -2)
        self.assertEqual(res, 0)
    
    def test_wrong_area(self):
        res = triangle.area(1, -2)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
