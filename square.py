
def area(a):
    """
    принимает длинну стороны квадрата, возвращает площадь этого квадрата
    print(square.area(5)) # -> 25
    """
    return a * a


def perimeter(a):
    """
    принимает длинну стороны квадрата, возвращает периметр этого квадрата
    print(square.perimeter(5)) # -> 20
    """
    return 4 * a


if __name__ == "__main__":
    print(area(5))
    print(perimeter(5))