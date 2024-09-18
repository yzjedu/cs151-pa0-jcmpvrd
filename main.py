# Programmer: Jordi Campoverde
# Course: CS151, Dr.Yalew
# Due Date: September 18, 2024
# Programming Assignment: PA 00
# Problem Statement: Calculates circular rug to see if there is enough space for rug in living room
# Data In: The radius of the rug
# Data Out: The area and circumference of the rug
# Credits: In Class
import math

#Prompt for a radius
radius_str = input("What is the radius of the rug:")
radius_int = int(radius_str)

#Apply the area formula
circle_area = math.pi * (radius_int ** 2)

#Apply the circumference formula
circle_circumference = 2 * math.pi * radius_int

#Output the results with formatting it to two decimal places
print (f"The circumference of the rug is:{circle_circumference:.2f}")
print (f"The area of the rug is: {circle_area:.2f}")


