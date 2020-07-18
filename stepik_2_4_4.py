def encoder(str1):
    current_symbol = str1[0]
    current_count = 1
    for s in str1[1:]:
        if current_symbol == s:
            current_count += 1
        else:
            print(current_symbol, current_count, sep="", end="")
            current_count = 1
            current_symbol = s
    print(current_symbol, current_count, sep="", end="")


arg = input()
encoder(arg)
