def serial_num_fibonacci(n):
    f0 = 0
    f1 = 1
    i = 0
    while f0 <= n:
        if n == f0:
            return i
        f0, f1 = f1, f0 + f1
        i += 1
    else:
        return -1


if __name__ == "__main__":
    arg = int(input())
    result = serial_num_fibonacci(arg)
    print(result)
