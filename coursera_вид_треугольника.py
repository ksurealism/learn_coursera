def triangle(a, b, c):
    squared_number_c = c ** 2
    squared_number_b = b ** 2
    squared_number_a = a ** 2
    sum_sq_a_b = squared_number_a + squared_number_b
    sum_sq_a_c = squared_number_a + squared_number_c
    sum_sq_b_c = squared_number_b + squared_number_c
    if a >= (c + b) or b >= (c + a) or c >= (a + b):
        return "impossible"
    if squared_number_c == sum_sq_a_b or \
            squared_number_b == sum_sq_a_c or \
            squared_number_a == sum_sq_b_c:
        return "rectangular"
    if squared_number_c > sum_sq_a_b or \
            squared_number_b > sum_sq_a_c or \
            squared_number_a > sum_sq_b_c:
        return "obtuse"
    if squared_number_c < sum_sq_a_b or \
            squared_number_b < sum_sq_a_c or \
            squared_number_a < sum_sq_b_c:
        return "acute"


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = int(input())
    arg3 = int(input())
    result = triangle(arg1, arg2, arg3)
    print(result)
