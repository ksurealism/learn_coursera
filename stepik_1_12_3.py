def calculator(a, b, s):
    """
    Функция, выполняющая заданную операцию над двумя числами

    :param a: Первый числовой аргумент
    :param b: Второй числовой аргумент
    :param s: Операция для вычисления
    :return: Результат вычисления калькулятора
    """
    # Сложение
    if s == "+":
        return a + b
    # Вычитание
    if s == "-":
        return a - b
    # Умножение
    if s == "*":
        return a * b
    # Деление на ноль
    if b == 0 and s == "/" or b == 0 and s == "div" or b == 0 and s == "mod":
        return "Деление на 0!"
    # Деление
    if s == "/":
        return a / b
    # Целочисленное деление
    if s == "div":
        return a // b
    # Взятие остатка от деления
    if s == "mod":
        return a % b
    # Возведение в степень
    if s == "pow":
        return a ** b
    # Неизвестная операция
    raise Exception("Unknown operation", s)


if __name__ == '__main__':
    arg1 = float(input())
    arg2 = float(input())
    arg3 = input()
    result = calculator(arg1, arg2, arg3)
    print(result)
