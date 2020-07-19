def conversion_a_to_b():
    a = int(input())
    b = int(input())
    while a > b:
        if (a % 2 == 0) and (a >= (b * 2)):
            a = a / 2
            print(":2")
        else:
            a = a - 1
            print("-1")


conversion_a_to_b()
