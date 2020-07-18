def sum_of_numbers():
    n = int(input())
    sum_of_num = n
    while n != 0:
        n = int(input())
        if n == 0:
            break
        sum_of_num += n
    print(sum_of_num)


sum_of_numbers()
