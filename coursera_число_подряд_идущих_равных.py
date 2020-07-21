def number_in_a_row_equal():
    n = int(input())
    k = n
    i = 1
    j_max = 1
    while n != 0:
        n = int(input())
        if n == k:
            i += 1
        else:
            i = 1
            k = n
        if i > j_max:
            j_max = i
    print(j_max)


number_in_a_row_equal()
