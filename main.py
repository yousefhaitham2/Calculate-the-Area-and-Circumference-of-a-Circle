# main.py

import math

# Take input from the user and assign it to the variable 'radius'
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference and area using the formulas
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Print the results
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")
