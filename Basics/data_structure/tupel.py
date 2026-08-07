# collection -> a single variable that can hold multiple values
# tuple() -> an ordered, immutable collection of elements (cannot be changed after creation)

# Creating a tuple
# Tuples are created using parentheses ()
my_tuple = ("apple", "banana", "cherry")
print(f"Tuple: {my_tuple}")

# Accessing elements
# You can access elements using their index (starting from 0)
print(f"First element: {my_tuple[0]}") # Output: apple
print(f"Last element: {my_tuple[-1]}") # Output: cherry (Negative indexing accesses from the end)

# Tuples are immutable
# Trying to change an element will result in an error
# my_tuple[0] = "orange"  
# This would cause a TypeError

# Tuple with a single element
# To create a tuple with one item, you MUST include a trailing comma
single_item_tuple = ("apple",)
not_a_tuple = ("apple") # This is just a string
print(f"Type of single_item_tuple: {type(single_item_tuple)}")
print(f"Type of not_a_tuple: {type(not_a_tuple)}")

# Tuple packing and unpacking
# Packing: Assigning multiple values to a single tuple variable
packed_tuple = 1, 2, "hello" # Parentheses are optional
# Unpacking: Assigning tuple values to multiple variables
a, b, c = packed_tuple
print(f"Unpacked values: a={a}, b={b}, c={c}")
