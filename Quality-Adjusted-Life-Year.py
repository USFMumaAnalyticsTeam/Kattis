n = int(input())
total = 0
for x in range(n):
    q,y = [float(number) for number in input().split()]
    prod = q * y
    total += prod
print(total)
