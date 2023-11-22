import unittest

def area(a, b):
    """
    принимает длины сторон прямоугольника, возвращает площадь этого прямоугольника
    print(rectangle.area(2, 5)) # -> 10
    """
    return a * b

def perimeter(a, b):
    """
    принимает длины сторон прямоугольника, возвращает периметр этого прямоугольника
    print(rectangle.perimeter(2, 5)) # -> 14
    """
    return 2 * (a + b)


if __name__ == "__main__":
    print(area(2, 5))
    print(perimeter(2, 5))