# -*- coding: utf-8 -*-
"""Death Grip.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hBZHd0mSAZBmGWs6MpPAIzbrGCMisZ3R
"""

n = int(input())
battle_information = []
if n!=(1<n and 1<n<100):
  pass
else: 
  quit()
for value in range(n):
  x = str(input())
  if (len(x) > 1000 and len(x)<1 ):
    quit() 
  else: 
    battle_information.append(x)

battle_information = [x.upper() for x in battle_information]

check_string = 'CD'

battles_won = 0 

for value in battle_information: 
  if not "CD" in value:
    battles_won += 1
print(battles_won)



# The hero does not win when: C does NOT follow D