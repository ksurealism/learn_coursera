from coursera_кирпичи_отверстие import is_brick_fit

assert is_brick_fit(1, 1, 1, 1, 1) == "YES", 'При входных 1, 1, 1, 1, 1 на выходе должно быть "YES"'
assert is_brick_fit(2, 2, 2, 1, 1) == "NO", 'При входных 2, 2, 2, 1, 1 на выходе должно быть "NO"'
assert is_brick_fit(6, 2, 7, 5, 6) == "YES", 'При входных 2, 3, 4, 5, 6 на выходе должно быть "YES"'
assert is_brick_fit(2, 3, 4, 1, 5) == "NO", 'При входных 2, 3, 4, 1, 5 на выходе должно быть "NO"'
