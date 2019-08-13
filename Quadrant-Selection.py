import sys
# Get user input
get_input_x = int(input())
get_input_y = int(input())
# Verify user input is postive or negative
x_positive = False
x_negative = False
y_positive = False
y_negative = False
# Initialize quadrant to 0
get_quadrant = 0
# Verify user has not entered 0, < -1000, or > 1000
if get_input_x == 0 or get_input_x < -1000 or get_input_x > 1000:
    sys.exit()
if get_input_y == 0 or get_input_y < -1000 or get_input_y > 1000:
    sys.exit()
# Check location of x and y as positive or negative
if(get_input_x) > 0:
    x_positive = True
elif(get_input_x) < 0:
    x_negative = True
if(get_input_y) > 0:
    y_positive = True
elif(get_input_y) < 0:
    y_negative = True
# Assign quadrant
if x_positive == True and y_positive == True:
    get_quadrant = 1
elif x_negative == True and y_positive == True:
    get_quadrant = 2
elif x_positive == True and y_negative == True:
    get_quadrant = 4
elif x_negative == True and y_negative == True:
    get_quadrant = 3
# Output
print(get_quadrant)

