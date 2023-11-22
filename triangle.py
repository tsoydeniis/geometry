def area(a, h):
    """
    принимет длинну стороны треугольника и длинну высоты, опущенной на эту сторону. возвращает площадь этого треугольника
    print(triangle.area(2, 5)) # -> 5.0
    """
    return a * h / 2

def perimeter(a, b, c):
    """
    принимает длины трёх сторон треугольника, возвращает периметр этого треугольника
    print(triangle.perimeter(2, 5, 7)) # -> 14
    """
    return a + b + c


if __name__ == "__main__":
    print(area(2, 5))
    print(perimeter(2, 5, 7))