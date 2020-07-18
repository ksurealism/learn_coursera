from coursera_шахматные_клетки import identical_chess_cells

assert identical_chess_cells(1, 1, 2, 2) == "YES", \
    "При входных данных 1, 1, 2, 2 на выходе должна быть строка 'YES'"
assert identical_chess_cells(1, 1, 2, 3) == "NO", \
    "При входных данных 1, 1, 2, 3 на выходе должна быть строка 'NO'"
assert identical_chess_cells(5, 3, 1, 5) == "YES", \
    "При входных данных 5, 3, 1, 5 на выходе должна быть строка 'YES'"
assert identical_chess_cells(3, 4, 8, 8) == "NO", \
    "При входных данных 3, 4, 8, 8 на выходе должна быть строка 'NO'"
