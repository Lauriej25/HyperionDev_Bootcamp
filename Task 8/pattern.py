
# #Practical task 1 
# Create two variables, to determain the number of stars and interations
 
num_stars=1 
rows=5

# Iterate through the range 0 to 2 * rows - 1
for i in range(0,2*rows):
    # Check if k is less than 4
    if i<4:
        # If true, print a string of '*' characters repeated 'num_stars' times
        print(("*"*num_stars))
        # Increase the value of 'a' by 1
        num_stars=  num_stars+1
    else:
        # If i is 4 or greater, print a string of '*' characters repeated 'num_stars' times
        print (("*"*num_stars))
        # Decrease the value of 'num_stars' by 1
        num_stars=num_stars-1
