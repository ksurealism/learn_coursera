def dick_knows_what_to_call_it():
    n = int(input())
    k = n
    i = 0
    while n != 0:
        n = int(input())
        if n != 0 and n > k:
            i += 1
        k = n
    print(i)


dick_knows_what_to_call_it()
