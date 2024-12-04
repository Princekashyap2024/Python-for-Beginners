# Problem :- create a function that returns both the area and circumference of a circle given its radius.

import math

def calculation(radius):
    parimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return parimeter, area

n = int(input("Enter the radius: "))
print(calculation(n))  # This will print the circumference of the circle
