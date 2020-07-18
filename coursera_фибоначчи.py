def fibonacci(n):
    f0 = 0
    f1 = 1
    i = 0
    while i < n:
        f0, f1 = f1, f0 + f1
        i += 1
    return f0


'''
def fibonacci_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
'''

if __name__ == "__main__":
    arg = int(input())
    result = fibonacci(arg)
    print(result)
