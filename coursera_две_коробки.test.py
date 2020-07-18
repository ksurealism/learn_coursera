from coursera_две_коробки import compare_boxes

assert compare_boxes(1, 2, 3, 3, 2, 1) == "Boxes are equal", \
    'При входных 1, 2, 3, 3, 2, 1 на выходе должно быть "Boxes are equal"'
assert compare_boxes(2, 2, 3, 3, 2, 1) == "The first box is larger than the second one", \
    'При входных 2, 2, 3, 3, 2, 1 на выходе должно быть \
    "The first box is larger than the second one"'
assert compare_boxes(1, 2, 3, 3, 2, 2) == "The first box is smaller than the second one", \
    'При входных 1, 2, 3, 3, 2, 2 на выходе должно быть \
    "The first box is smaller than the second one"'
assert compare_boxes(7, 6, 3, 8, 4, 5) == "Boxes are incomparable", \
    'При входных 7, 6, 3, 8, 4, 5 на выходе должно быть "Boxes are incomparable"'
