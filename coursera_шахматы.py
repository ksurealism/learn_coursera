def chess(x_1, y_1, x_2, y_2):
    if (x_1 + 1 == x_2 or x_1 - 1 == x_2 or x_1 == x_2) \
            and (y_1 + 1 == y_2 or y_1 - 1 == y_2 or y_1 == y_2):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    arg1 = int(input())
    arg2 = int(input())
    arg3 = int(input())
    arg4 = int(input())
    result = chess(arg1, arg2, arg3, arg4)
    print(result)
