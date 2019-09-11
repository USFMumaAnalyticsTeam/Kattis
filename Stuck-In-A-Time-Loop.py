import sys
n= int(input())
if n<1 or n>100:
    sys.exit()
for i in range(n):
    print(f'{i+1} Abracadabra')
