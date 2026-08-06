x = 3.14
y = 4.71
z = 10


# round() = rounds the number to the nearest integer
print(f"Round of {x}: {round(x)}") # 3
print(f"Round of {y}: {round(y)}") # 5
print(f"Round of {z}: {round(z)}") # 10

# floor() = rounds the number down to the nearest integer
import math # importing math module to use floor() function
print(f"Floor of {x}: {math.floor(x)}") # 3
print(f"Floor of {y}: {math.floor(y)}") # 4

# ceil() = rounds the number up to the nearest integer
print(f"Ceil of {x}: {math.ceil(x)}") # 4
print(f"Ceil of {y}: {math.ceil(y)}") # 5

# sqrt() = returns the square root of a number
print(f"Square root of {z}: {math.sqrt(z)}") # 3.1622776601683795

# pow() = returns the value of x to the power of y
print(f"{x} to the power of {y}: {math.pow(x, y)}") # 3.14 to the power of 4.71: 306.019684

# abs() = returns the absolute value of a number
print(f"Absolute value of -{z}: {abs(-z)}") # 10


# max() = returns the largest number
print(f"Maximum of {x}, {y}, and {z}: {max(x, y, z)}") # 10

# min() = returns the smallest number
print(f"Minimum of {x}, {y}, and {z}: {min(x, y, z)}") # 3.14

