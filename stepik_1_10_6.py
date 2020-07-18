def main(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return "Високосный"
    else:
        return "Обычный"


if __name__ == "__main__":
    arg1 = int(input())
    result = main(arg1)
    print(result)
