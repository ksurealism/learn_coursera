from coursera_is_power_of_two import is_power_two

assert is_power_two(1) == "YES", "При значении 1 должна возвращаться строка 'YES'"
assert is_power_two(2) == "YES", "При значении 2 должна возвращаться строка 'YES'"
assert is_power_two(8) == "YES", "При значении 8 должна возвращаться строка 'YES'"
assert is_power_two(12) == "NO", "При значении 12 должна возвращаться строка 'NO'"
assert is_power_two(6) == "NO", "При значении 6 должна возвращаться строка 'NO'"
assert is_power_two(0) == "NO", "При значении 0 должна возвращаться строка 'NO'"
assert is_power_two(3) == "NO", "При значении 3 должна возвращаться строка 'NO'"
