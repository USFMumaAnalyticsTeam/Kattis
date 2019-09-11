# Storing input:
# N as 'swords' integer
# Slats as 'TBLR' multidimensional list

swords = int(input())
TBLR = list()
for sword in range(swords):
    numbers = str(input())
    TBLR.append([int(digit) for digit in numbers])

# Counting total TB and LR slats

TB = 0
LR = 0
for sword in range(swords):
    for digit in range(len(TBLR[sword])):
        if digit == 0 or digit == 1:
            if TBLR[sword][digit] == 0:
                TB = TB + 1
        elif digit == 2 or digit == 3:
            if TBLR[sword][digit] == 0:
                LR = LR + 1

# Constructing new swords:

# Determining how many complete TB and LR pairs we have
TB_complete = TB // 2
LR_complete = LR // 2

# Determining how many swords we can make with complete TB and LR pairs
total_swords = 0
if TB_complete <= LR_complete:
    total_swords = TB_complete
else:
    total_swords = LR_complete

# Determining remaining slabs
TB_remaining = TB - (total_swords * 2)
LR_remaining = LR - (total_swords * 2)

# Printing output

print(f'{total_swords} {TB_remaining} {LR_remaining}')
