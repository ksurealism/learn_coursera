def number_of_highs():
    n = int(input())
    number = n
    i = 1
    while n != 0:
        n = int(input())
        if number < n:
            number = n
            i = 1
        elif number == n:
            i += 1
        else:
            pass
    print(i)


number_of_highs()
