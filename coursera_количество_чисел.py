def number_of_entered_numbers():
    n = int(input())
    i = 1
    if n == 0:
        i = 0
    while n != 0:
        n = int(input())
        if n == 0:
            break
        else:
            i += 1
    print(i)


number_of_entered_numbers()
