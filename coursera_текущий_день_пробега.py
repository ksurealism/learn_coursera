def current_day_of_run(x, y):
    i = 1
    mileage = x
    while mileage < y:
        mileage *= 1.1
        i += 1
    return i


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = int(input())
    result = current_day_of_run(arg1, arg2)
    print(result)
