#Ask the user to enter their age
# Working from the highest variable number working down in accending order
age = int(input("Please input your age: "))
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy retirement!")
elif age >= 40:
    print("Your over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount")
else:
    print("Age is but a number.")
