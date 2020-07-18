def is_power_two(n):
    i = 1
    if n == 1:
        return "YES"
    while i <= n:
        i *= 2
        if i == n:
            return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    arg = int(input())
    result = is_power_two(arg)
    print(result)
