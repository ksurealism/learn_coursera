def smallest_number_divisor():
    n = int(input())
    minim = 2
    while n % minim != 0:
        minim += 1
    else:
        print(minim)


smallest_number_divisor()
