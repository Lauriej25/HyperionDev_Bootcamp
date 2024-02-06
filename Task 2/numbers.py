#Ask user to enter 3 numbers and store them as integers
num_1 = (int(input ("Enter a number :")))
num_2 = (int(input ("Enter another number :")))
num_3 = (int(input ("Enter final number :")))
#Print the sum of all the numbers (num_1 + num_2 + num_3 = )
sum_of_all_numbers = (num_1 + num_2 + num_3)
print ("The sum of all numbers entered is ", num_1, " + ", num_2, " + ", num_3, " = ",(sum_of_all_numbers) )
#Print the first number minus the second (num_1 - num_2 = )
print ("Your first number minus by your second number is ", num_1, " - ", num_2, " = ", (num_1 - num_2))
#Print the third number multiplies by the 1st number (num_3 * num_1 = )
print ("Your third number multiplied by your first number is ",num_3, " * ", num_1, " = ", num_3 * num_1)
#Print the sum of all three numbers divided by the third number (number_selections / num_3 = )
#Cast number to a float and round to 2 decimal places
print ("The sum of all your numbers devided by your third number is ", sum_of_all_numbers, " / ", num_3, " = ",  (round(float(sum_of_all_numbers / num_3),2)))
