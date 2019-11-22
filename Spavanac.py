'''
This python code is meant to receive a time stamp,
in 24-hour notation and print out a new time stamp,
45 minutes earlier, also in 24-hour notation
'''

# function to calculate minutes
def minutes(x,y):
    newMin = (x - 45) + y
    return newMin

# receives input from single line
# and splits into 2 different variables
ab = input().split()
h = int(ab[0])
m = int(ab[1])

# minute 45 or greater
if m > 44:
    m = minutes(m,0)
# hour 0
elif h == 0:
    m = minutes(m,60)
    h = 23
else:
    m = minutes(m,60)
    h = h-1

print(h, m)
