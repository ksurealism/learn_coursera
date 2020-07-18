from util.parse_number import get_units_from_number, get_two_digit_number_from_number


def name_of_programmers(n):
    two_digit_number = get_two_digit_number_from_number(n)
    if two_digit_number == 11 or two_digit_number == 12 \
            or two_digit_number == 13 or two_digit_number == 14:
        return str(n) + " " + "программистов"
    get_units_number = get_units_from_number(n)
    if get_units_number == 5 or get_units_number == 0:
        return str(n) + " " + "программистов"
    if get_units_number == 1:
        return str(n) + " " + "программист"
    if get_units_number == 6 or get_units_number == 7 \
            or get_units_number == 8 or get_units_number == 9:
        return str(n) + " " + "программистов"
    else:
        return str(n) + " " + "программиста"


if __name__ == "__main__":
    arg = int(input())
    result = name_of_programmers(arg)
    print(result)
