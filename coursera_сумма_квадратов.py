def sum_of_squares():
    n = int(input())
    i = 1
    sum_of_sq = 0
    while i <= n:
        sum_of_sq += i ** 2
        i = i + 1
    print(sum_of_sq)


sum_of_squares()
