def reverse_number(n):
    new_num = 0
    while n > 0:
        new_num = (new_num * 10) + (n % 10)
        n = n // 10
    return new_num


def number_of_palindromes():
    k = int(input())
    count = 0
    i = 1
    while i <= k:
        if i == reverse_number(i):
            count += 1
        i += 1
    print(count)


number_of_palindromes()
