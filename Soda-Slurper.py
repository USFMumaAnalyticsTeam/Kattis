e, f, c = [int(num) for num in input().split()]
drunk_bottles = 0
e +=f 
while e >= c: 
  remainder_bottles = e%c 
  e = e//c
  drunk_bottles += e
 

  e += remainder_bottles

  
print(drunk_bottles)
