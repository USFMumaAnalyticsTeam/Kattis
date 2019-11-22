# This python code is meant to take the day and month
# integer from the date class and output the
# corresponding weekday in the year of 2009

# Import date class
from datetime import date

# Retrieve user input as two positive integers
# to represent day and month
day, month = [int(s) for s in input().split()]

# Retrieve weekday from day and month in the year 2009
date = date(2009, month, day)

# Create a weekday list
days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
]
# Print Weekday
print(days[date.weekday()])