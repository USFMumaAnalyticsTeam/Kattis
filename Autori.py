# This python code is meant to take a single string that is in a
# long naming variation (ex. Apple-Boy-Cat) and change it
# to a short variation (ex. ABC)

import sys
# Receive user input as string
long_var = input()

# Verify user input is no more than 100 characters
if (long_var.count('') > 100):
    sys.exit()

# Create an empty list
my_list = []

# Go through each letter in string
# and check if it's uppercase
# If so add to list
for letter in long_var:
    if (letter.isupper()) == True:
        my_list.append(letter)

# print list
print ("".join(my_list))