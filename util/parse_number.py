def get_units_from_number(n):
    k = n % 100
    answer = k % 10
    return answer


def get_two_digit_number_from_number(n):
    return n % 100


def get_number_by_position(n, x):
    decimal_pow = 10 ** x
    i = n // decimal_pow
    return get_units_from_number(i)

