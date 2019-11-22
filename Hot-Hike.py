# length of vacation
n = int(input())
if n < 3 or n > 50:
    sys.exit()

# max temp for each vacation day
t = [int(number) for number in input().split()]
for y in t:
    if y < -20 or y > 40:
        sys.exit()

# empty dictionary
val = {}

# grabs max temp on hiking days and start day and adds to dictionary
for x in range(0,n-2):
    forward = t[x]
    back = t[x+2]
    check = max(forward,back)
    val[x] = check
        
# grabs lowest temperature and corresponding day from dictionary
final_temp = min(val.values())
final_day = min(val, key=val.get)+1

# grabs day from new list
print(final_day, final_temp)
