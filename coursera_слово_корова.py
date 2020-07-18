def get_units_from_number(n):
    k = n % 100
    answer = k % 10
    return answer


def ending_the_word_cow():
    n = int(input())
    remainder = get_units_from_number(n)
    if n == 0 or 4 < n < 15 or remainder == 0 \
            or 4 < remainder < 15:
        print(str(n) + ' korov')
    elif n == 1 or remainder == 1:
        print(str(n) + ' korova')
    else:
        print(str(n) + ' korovy')


ending_the_word_cow()
