# conditional expression = a shorter way of writing an if else statement (ternary operator)
# Print or assign one of two values based on a condition in a single line of code
# X if condition else Y

num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd") # prints "Even" if the number is even, otherwise prints "Odd"

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
# Find the maximum of the two numbers using a conditional expression
maximum = first_number if first_number > second_number else second_number
print(f"The maximum number is: {maximum}")