from util.parse_number import get_units_from_number, get_two_digit_number_from_number, get_number_by_position

assert get_units_from_number(9) == 9, "Units for number 9 should be "
assert get_units_from_number(63) == 3, "Units for number 63 should be 3"
assert get_units_from_number(476) == 6, "Units for number 476 should be 6"
assert get_units_from_number(7574) == 4, "Units for number 7574 should be 4"

assert get_two_digit_number_from_number(564) == 64, "Units for number  should be "
assert get_two_digit_number_from_number(3463) == 63, "Units for number  should be "

assert get_number_by_position(90234, 0) == 4, "Для числа 90234 цифра нулевой позиции должна быть 4"
assert get_number_by_position(90234, 4) == 9, "Для числа 90234 цифра 4 позиции должна быть 9"
assert get_number_by_position(190234, 10) == 0, "Для числа 190234 цифра 10 позиции должна быть 0"

