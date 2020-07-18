def is_brick_fit(a, b, c, d, e):
    if (a <= d) and (b <= e) or (b <= d) and (a <= e):
        return "YES"
    if (b <= d) and (c <= e) or (c <= d) and (b <= e):
        return "YES"
    if (a <= d) and (c <= e) or (c <= d) and (a <= e):
        return "YES"
    return "NO"


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = int(input())
    arg3 = int(input())
    arg4 = int(input())
    arg5 = int(input())
    result = is_brick_fit(arg1, arg2, arg3, arg4, arg5)
    print(result)
