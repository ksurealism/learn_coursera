def binary_logarithm(n):
    k = 0
    x = 1
    while x < n:
        k += 1
        x *= 2
    return k


if __name__ == "__main__":
    arg = int(input())
    result = binary_logarithm(arg)
    print(result)
