# Ask user to enter their favourite restraunt
string_fav = input("What is your favourite restraunt? ")
# Ask user to enter their favourite number and cast it as an integer
int_fav = int(input("What is your favourite number? "))
print ("Your favourite restraunt is: ", string_fav)
print (("Your favourite number is: "), (int_fav))
# Try to change string_fav to an integer - This does not work as the input will not be a valid literal
string_fav = int(input("What is your favourite restraunt? "))
