a, b, c = int(input()), int(input()), int(input())
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)
