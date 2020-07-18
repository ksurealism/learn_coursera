def identical_chess_cells(x1, y1, x2, y2):
    if (x1 % 2 == x2 % 2 and y1 % 2 == y2 % 2) or \
            (x1 % 2 != x2 % 2 and y1 % 2 != y2 % 2):
        return "YES"
    else:
        return "NO"


def checkers(x1, y1, x2, y2):
    colour = identical_chess_cells(x1, y1, x2, y2)
    delta_y = (y2 - y1) >= (x2 - x1)
    if (colour == "YES") and (y2 > y1) and delta_y:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = int(input())
    arg3 = int(input())
    arg4 = int(input())
    result = checkers(arg1, arg2, arg3, arg4)
    print(result)
