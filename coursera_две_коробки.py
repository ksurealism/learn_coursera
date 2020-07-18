def sort_numbers(a, b, c):
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c


def compare_boxes(a1, b1, c1, a2, b2, c2):
    str_is_equal = "Boxes are equal"
    str_is_first_larger = "The first box is larger than the second one"
    str_is_first_smaller = "The first box is smaller than the second one"
    min1, mid1, max1 = sort_numbers(a1, b1, c1)
    min2, mid2, max2 = sort_numbers(a2, b2, c2)
    if min1 == min2 and mid1 == mid2 and max1 == max2:
        return str_is_equal
    if min1 >= min2 and mid1 >= mid2 and max1 >= max2:
        return str_is_first_larger
    if min1 <= min2 and mid1 <= mid2 and max1 <= max2:
        return str_is_first_smaller
    return "Boxes are incomparable"


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = int(input())
    arg3 = int(input())
    arg4 = int(input())
    arg5 = int(input())
    arg6 = int(input())
    result = compare_boxes(arg1, arg2, arg3, arg4, arg5, arg6)
    print(result)
