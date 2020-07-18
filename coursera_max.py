n = int(input())
maxim = n
while n != 0:
    n = int(input())
    if n == 0:
        break
    if maxim < n:
        maxim = n
print(maxim)
