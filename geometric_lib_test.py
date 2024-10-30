import unittest
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle


class TestGeometricLib(unittest.TestCase):
    #Так как в формулах для нахождения площади и периметра круга используется пи, оставим только целую часть 
    def test_circle_area(self):
        self.assertEqual(Circle.area(3) // 1, 28)
        self.assertEqual(Circle.area(10) // 1, 314)

    def test_circle_perimeter(self):
        self.assertEqual(Circle.perimeter(3) // 1, 18)
        self.assertEqual(Circle.perimeter(10) // 1, 62)

    def test_rectangle_area(self):
        self.assertEqual(Rectangle.area(5, 6), 30)
        self.assertEqual(Rectangle.area(10, 17), 170)

    def test_rectangle_perimeter(self):
        self.assertEqual(Rectangle.perimeter(5, 6), 22)
        self.assertEqual(Rectangle.perimeter(10, 17), 54)

    def test_square_area(self):
        self.assertEqual(Square.area(3), 9)
        self.assertEqual(Square.area(10), 100)

    def test_scuare_perimeter(self):
        self.assertEqual(Square.perimeter(3), 12)
        self.assertEqual(Square.perimeter(10), 40)
    
    def test_triangle_area(self):
        self.assertEqual(Triangle.area(3, 2), 3)
        self.assertEqual(Triangle.area(10, 15), 75)

    def test_triangle_perimeter(self):
        self.assertEqual(Triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(Triangle.perimeter(10, 15, 23), 48)

if __name__ == "__main__":
  unittest.main()