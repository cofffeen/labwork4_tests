import unittest

def area(a, b): 
    # принимает числа a и b, возвращает площадь прямоугольника со сторонами a, b
    return a * b 

def perimeter(a, b): 
    # принимает числа a и b, возвращает периметр прямоугольника со сторонами a, b
    return (a + b)*2 

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(1, 2)
        self.assertEqual(res, 2)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(1, 2)
        self.assertEqual(res, 6)

if __name__ == '__main__':
    unittest.main()
