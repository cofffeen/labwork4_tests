import unittest

def area(a, h): 
    # принимает числа a и h, возвращает площадь треугольника со стороной a и высотой h
    return a * h / 2 

def perimeter(a, b, c): 
    # принимает числа a, b и c, возвращает периметр треугольника со сторонами a, b и c
    return a + b + c 

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(1, 2)
        self.assertEqual(res, 1)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)


    def test_perimeter(self):
        res = perimeter(1, 2, 2)
        self.assertEqual(res, 5)

if __name__ == '__main__':
    unittest.main()
