# Import math function to complete equation
import math
#Ask user to enter the sides of a 3 side of a triangle to find the area
print ("To find out the area of a triangle enter all three lengths of a triangle in millimetres (a, b, c)")
side_a = int(input("Enter lenght of side a: "))
side_b = int(input("Enter lenght of side b: "))
side_c = int(input("Enter lenght of side c: "))
s = (side_a + side_b + side_c)/2
area = (math.sqrt(s * (s-side_a) * (s-side_b) * (s-side_c)))
print ("The area of you triangle is: ", (round(area,2)), "mm squared")
