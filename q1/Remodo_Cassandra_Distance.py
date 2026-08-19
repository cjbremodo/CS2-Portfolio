from math import sqrt, pow

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print(f"The distance between the two points is: {distance:.2f}")

# Reflection:
# Using the math library made the program easier because I did not need
# to create my own square root and exponent functions. The sqrt() and
# pow() functions helped me calculate the distance accurately and quickly.
