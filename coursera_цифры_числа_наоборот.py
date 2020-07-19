def reverse_number():
    n = int(input())
    new_num = 0
    while n > 0:
        new_num = (new_num * 10) + (n % 10)
        n = n // 10
    print(new_num)


reverse_number()
