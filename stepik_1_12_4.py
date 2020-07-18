pi = 3.14

def calc_triangle_area(a, b, c):
    p = (a + b + c) / 2
    s2 = p * (p - a) * (p - b) * (p - c)
    s = s2 ** 0.5
    return s


def calc_rectangle_area(a, b):
    s = a * b
    return s


def calc_circle_area(r):
    s = pi * r ** 2
    return s


if __name__ == "__main__":
    kind = input()
    if kind == "треугольник":
        arg1 = int(input())
        arg2 = int(input())
        arg3 = int(input())
        result = calc_triangle_area(arg1, arg2, arg3)
        print(result)
    if kind == "прямоугольник":
        arg1 = int(input())
        arg2 = int(input())
        result = calc_rectangle_area(arg1, arg2)
        print(result)
    if kind == "круг":
        arg1 = int(input())
        result = calc_circle_area(arg1)
        print(result)

