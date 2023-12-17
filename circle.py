import math


def area(r):
    """
    принимает длинну радиуса окружности, возвращает площадь этой окружности
    print(circle.area(5)) # -> 78.53981633974483
    """
    return r * r * math.pi


def perimeter(r):
    """
    принимает длинну радиуса окружности, возвращает периметр этой окружности
    print(circle.perimeter(5)) # -> 31.41592653589793
    """
    return r * 2 * math.pi


if __name__ == "__main__":
    print(area(5))
    print(perimeter(5))