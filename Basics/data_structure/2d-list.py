# 2d list -> A list of lists, often used to represent a grid, table, or matrix.

# Individual 1D lists (Rows)
fruits = ["apple", "orange", "banana"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# Combining them into a 2D List
# This creates a 3x3 grid (3 rows, 3 columns)
food_grocery = [fruits, vegetables, meats]

# Visualizing the 2D List:
# Row 0 (fruits)     : ["apple", "orange", "banana"]
# Row 1 (vegetables) : ["celery", "carrots", "potatoes"]
# Row 2 (meats)      : ["chicken", "fish", "turkey"]

# Accessing Elements
# Syntax: list_name[row_index][column_index]
print("Row 0, Col 0:", food_grocery[0][0])  # Output: 'apple'
print("Row 1, Col 2:", food_grocery[1][2])  # Output: 'potatoes'
print("Row 2, Col 1:", food_grocery[2][1])  # Output: 'fish'

# Iterating Through a 2D List
print("\nAll items in the 2D List:")
for row in food_grocery:        # Loop through each row
    for item in row:            # Loop through each item in the current row
        print(item, end=" ")
    print()                     # Print a newline after finishing a row