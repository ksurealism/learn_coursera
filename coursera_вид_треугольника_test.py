from coursera_вид_треугольника import triangle

assert triangle(3, 4, 5) == "rectangular", 'При входных данных 3, 4, 5 должна выводиться строка "rectangular"'
assert triangle(3, 5, 4) == "rectangular", 'При входных данных 3, 5, 4 должна выводиться строка "rectangular"'
assert triangle(3, 4, 4) == "acute", 'При входных данных 3, 4, 4 должна выводиться строка "acute"'
assert triangle(2, 3, 5) == "impossible", 'При входных данных 2, 3, 5 должна выводиться строка "impossible"'
assert triangle(3, 1, 1) == "impossible", 'При входных данных 3, 1, 1 должна выводиться строка "impossible"'
assert triangle(6, 5, 3) == "obtuse", 'При входных данных 3, 1, 1 должна выводиться строка "obtuse"'
