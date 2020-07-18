def intervals(n):
    """
    Программа, принимающую на вход целое число, которая выводит True,
    если переданное значение попадает в интервал
    """
    if -15 < n <= 12 or 14 < n < 17 or n >= 19:
        return True
    else:
        return False


if __name__ == '__main__':
    arg = int(input())
    result = intervals(arg)
    print(result)
