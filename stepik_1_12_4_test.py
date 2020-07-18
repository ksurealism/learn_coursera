from stepik_1_12_4 import calc_circle_area, calc_rectangle_area, calc_triangle_area

assert calc_triangle_area(3, 4, 5) == 6.0, "Площадь треугольника со сторонами 3, 4, 5 должна быть равна 6"
assert calc_rectangle_area(4, 10) == 40.0, "Площадь прямоугольника со сторонами 4, 10 должна быть равна 40.0"
assert calc_circle_area(5) == 78.5, "Площадь круга с радиусом 5 должна быть равна 78.5"
