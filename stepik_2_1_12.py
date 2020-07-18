def least_divisible(n, k):
    if n > k:
        x = n
    else:
        x = k
    while x <= n * k:
        if x % n == 0 and x % k == 0:
            return x
        else:
            x += 1


if __name__ == '__main__':
    arg1 = int(input())
    arg2 = int(input())
    result = least_divisible(arg1, arg2)
    print(result)
