arr1 = map(int, input().split())
arr2 = map(int, input().split())
arr3 = map(int, input().split())
arr4 = map(int, input().split())
arr5 = map(int, input().split())

x1 = sum(arr1)
x2 = sum(arr2)
x3 = sum(arr3)
x4 = sum(arr4)
x5 = sum(arr5)

max_list = [x1, x2, x3, x4, x5]
max = max(max_list)

if x1 == max:
    print(1, x1)
elif x2 == max:
    print(2, x2)
elif x3 == max:
    print(3, x3)
elif x4 == max:
    print(4, x4)
else:
    print(5, x5)




