Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n, m = input().split()
n = int(n)
m = int(m)

if n == m:
  print (n+1)

if n > m:
  for i in range(m+1, n+2):
    print (i)
  
if m > n:
  for i in range(n+1, m+2):
    print (i)
