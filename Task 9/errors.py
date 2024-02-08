# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #Syntax error, added parentheses  
print ("\n") #Syntax error, added parentheses and removed the unnecessary indent

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = ("24") #Syntax error - added parentheses, removed the unnecessary indent & runtime error - for line 11 removed "years_old"
age = int(age_Str) #Syntax error - removed the unnecessary indent & runtime error - casted str to an int
print("I'm" , age , "years old.") #Syntax error - added parentheses & runtime error - can not concatenate str replaced "+" with "," 

# Variables declaring additional years and printing the total years of age
years_from_now = int("3") #Syntax error - removed the unnecessary indent
total_years = age + years_from_now #Syntax error - removed the unnecessary indent & runtime error - casted the str to a int on line 14

print ("The total number of years:" , total_years) #Syntax error - added parentheses & a logical/syntax error - "answer_years" changed  
                                                   # to total_years removing quotation marks, and the "+" replaced with "," 
# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6 #Syntax error - total needs to be total_years
print ("In 3 years and 6 months, I'll be " , total_months , " months old") #Syntax error - added parentheses, runtime error - trying to add
                                                                           # a int to a str, removed quotation marks and replaced "+" with ","  
                                                                           # & logical error as it is missing the extra 6 months stated in the string
                                                                           # "+ 6" was added to get the correct answer
#HINT, 330 months is the correct answer

