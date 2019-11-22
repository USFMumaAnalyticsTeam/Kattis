'''
This python code is meant to find the minimum number of gold coins
needed to pay the knights to slay the dragons invading loowater, or
if the knights are unable to, signal loowater is doomed. A knight can
slay a dragon if his height is as tall as the diameter of the dragon's
neck and the knight is paid his height in gold.
'''

import sys

# function that returns an answer for each test case
def loowater(h,k,l1,l2):
    doomed = False
    gold = 0
    current_knight = 0
    current_head = 0
    
    # sort from smallest to largest value and enter in a new list
    diameter_list = sorted(l1)
    height_list = sorted(l2)

    # repeat for as many heads you have
    # match a knight to every head
    while current_head < h:
        
        # if there are more heads than knights available, loowater is doomed
        if k < h:
            doomed = True
            break
        elif current_knight == k or current_head == h:
            doomed = True
            break

        # if current knight can chop current head
        # add knights height in gold and move on to the next knight & head
        elif height_list[current_knight] >= diameter_list[current_head]:
            gold += height_list[current_knight]
            current_knight += 1
            current_head += 1

        # if current knight cannot chop current head, move on to next knight and try again
        # if you run out of knights, loowater is doomed
        else:
            if current_knight == k-1:
                doomed = True
                break
            current_knight += 1
    if doomed:
        answer = "Loowater is doomed!"
    else:
        answer = gold
    return answer

# repeats until signal for last test case is given
while True:

    list1 = []
    list2 = []
    heads, knights = map(int, input().split())
    if heads < 1 or heads > 20000:
        sys.exit()
    if knights < 1 or knights > 20000:
        sys.exit()
    for x in range(0,heads):
        list1.append(int(input()))
        if list1[x] < 0 or list1[x] > 10000:
            sys.exit()
    for y in range(0,knights):
        list2.append(int(input()))
        if list2[y] < 0 or list2[y] > 10000:
            sys.exit()
            
    # executes function with input values
    output = loowater(heads,knights,list1,list2)
    print(output)

