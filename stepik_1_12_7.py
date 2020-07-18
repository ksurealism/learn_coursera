from util.parse_number import get_number_by_position, get_units_from_number


def lucky_ticket(n):
    n = int(n)
    last_digit = get_number_by_position(n, 0)
    penultimate_digit = get_number_by_position(n, 1)
    first_digit_from_the_end = get_number_by_position(n, 2)
    third_digit = get_number_by_position(n, 3)
    second_digit = get_number_by_position(n, 4)
    first_digit = get_number_by_position(n, 5)
    _sum_of_first_dig = first_digit + second_digit + third_digit
    _sum_of_last_dig = first_digit_from_the_end + penultimate_digit + last_digit
    if _sum_of_first_dig == _sum_of_last_dig:
        return "Счастливый"
    else:
        return "Обычный"


if __name__ == "__main__":
    arg = input()
    result = lucky_ticket(arg)
    print(result)
