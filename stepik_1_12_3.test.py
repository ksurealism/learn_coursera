from stepik_1_12_3 import calculator

assert calculator(3, 5, "+") == 8, "3 + 5 должно быть равно 8"
assert calculator(125, 4, "-") == 121, "125 - 4 должно быть равно 121"
assert calculator(5, 7, "*") == 35, "7 * 5 должно быть равно 35"
assert calculator(1, 0, "/") == "Деление на 0!", "при делении на 0 должна возвращаться ошибка"
assert calculator(6, 4, "/") == 1.5, "6 / 4 должно быть равно 1.5"
assert calculator(6, 0, "div") == "Деление на 0!", "при целочисленном делении на 0 должна возвращаться ошибка"
result7 = calculator(8, 4, "div")
assert result7 == 2, "8 div 4 должно быть равно 2, а возвращается " + result7
assert calculator(13, 0, "mod") == "Деление на 0!", "при взятии остатка от деления на 0 должна возвращаться ошибка"
assert calculator(13, 6, "mod") == 1, "13 % 6 должно быть равно 1"
assert calculator(3, 2, "pow") == 9, "3 ** 2 должно быть равно 9"
