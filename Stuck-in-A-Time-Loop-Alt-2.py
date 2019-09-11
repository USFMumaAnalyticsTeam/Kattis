#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Programmer: Brennan Harrison
# Date: 09/06/2019
# Problem ID: timeloop

# Get user input
n = int(input())

# Initialize counter variable
x = 1

# Test user input
if n >= 1 and n<=100:
    
    # Iterate for the same number of times as the magic number
    while (x <= n):
        print(str(x) + " Abracadabra") # Print the user's output
        x = x + 1 # Increment the counter variable

