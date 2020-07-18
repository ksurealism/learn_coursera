a = int(input())
b = int(input())
c = a
i = 0
while i != b:
    if c % 2 == 0:
        c = a / 2
    else:
        c = a - 1
    i += 1
print(c)
