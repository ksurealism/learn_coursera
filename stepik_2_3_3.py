"""
Таблица умножения
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d + 1):
    print("\t", i, end="")
print("")
for row in range(a, b + 1):
    print(row, end="")
    for col in range(c, d + 1):
        print("\t", col * row, end="")
    print("")
