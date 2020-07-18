def square_number():
    n = int(input())
    i = 1
    while i <= (n ** 0.5):
        sq = i ** 2
        print(str(sq) + " ", end="")
        i += 1


square_number()
