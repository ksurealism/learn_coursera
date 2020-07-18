def coordinate_quarter(x, y, x2, y2):
    if (x > 0) == (x2 > 0) and (y > 0) == (y2 > 0):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = int(input())
    arg3 = int(input())
    arg4 = int(input())
    result = coordinate_quarter(arg1, arg2, arg3, arg4)
    print(result)
