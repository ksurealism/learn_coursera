def apartments(x, y):
    number_of_apartments = (y + 1) - x
    previous_apartments = x - 1
    if x == 1:
        return "YES"
    if previous_apartments % number_of_apartments == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = int(input())
    result = apartments(arg1, arg2)
    print(result)
