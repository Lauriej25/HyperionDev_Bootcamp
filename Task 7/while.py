# Task 7
# Ask the user to input a number and continute to enter new numbers unitl "-1" is entered
# Print the average of all numbers entered 
count = 0
total = 0

user_input = int(input("Please enter a number (-1 to exit) :"))

# Add a variable to count the number of entries and a variable to count the total of all entries
while user_input != -1:
    total += user_input
    count += 1

    user_input = float(input("Please enter a number (-1 to exit) :"))

    if user_input == -1:
        average = total/count
        print (f"The average of all your selected numbers is: {average}")
        break
