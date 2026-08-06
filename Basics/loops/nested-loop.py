# nested loop -> a loop inside another loop, where the inner loop runs completely for each iteration of the outer loop
# this is a nested loop that prints a multiplication table from 1 to 10
for i in range(1, 11):  # outer loop for the first number (1 to 10)
    for j in range(1, 11):  # inner loop for the second number (1 to 10)
        product = i * j  # calculates the product of the two numbers
        print(f"{i} x {j} = {product}")  # prints the multiplication result
    print()  # prints a new line after each row of the multiplication table
    
# *
# * * 
# * * *
# * * * *
for i in range(1, 5):  # outer loop for the number of rows
    for j in range(1, i + 1):  # inner loop for the number of stars in each row
        print("*", end=" ")  # prints a star without a new line
    print()  # prints a new line after each row of stars


# 1 
# 1 2
# 1 2 3
for i in range(1, 4):  # outer loop for the number of rows
    for j in range(1, i + 1):  # inner loop for the numbers in each row
        print(j, end=" ")  # prints the number without a new line
    print()  # prints a new line after each row of numbers
    
