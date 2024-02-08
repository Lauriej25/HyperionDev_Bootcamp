# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


animal = ("Lion") # A syntax error has occured as quotation marks are missing , which will not define the string
animal_type = ("cub")
number_of_teeth = 16
# Below A Logical error and Syntax error has occured due to the string not being formated and "number_of_teeth" and "animal_teeth" are in the incorrect postions
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # The "f" has been added to format ths sting, "number_of_teeth" and "animal_teeth" have been swaped to read correctly

print (full_spec)
