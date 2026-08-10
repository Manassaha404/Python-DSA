
# Recursion Theory:
# A function calling itself to solve a smaller instance of the same problem.
# Key components:
# 1. Base Case: Condition to stop recursion (prevents infinite loop).
# 2. Recursive Case: Function calls itself with arguments moving toward the base case.


def factorial(n):
    # 1. Base case
    if n == 0 or n == 1:
        return 1
    # 2. Recursive case
    return n * factorial(n - 1)

print(f"Factorial of 5 is: {factorial(5)}")