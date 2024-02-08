# This program is designed to calculate the average of three numbers.
# The code below will cause a logical error

# User inputs three numbers
# To correct the locical error the three inputs below need to be casted to floats so they are added together
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
number3 = input("Enter the third number: ")

# Calculate the average
# The error is causing the three numbers to be combined and not added together
# Eg - 1 + 1 + 1 = 111 instead of 1 + 1 + 1 = 3
average = float(number1 + number2 + number3) / 3


# Display the result
print("The average of the three numbers is: " + str(average))
