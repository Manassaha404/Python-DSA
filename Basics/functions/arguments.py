# ------------------ Default Arguments in Python ------------------
# Theory:
# 1. You can provide a default value to a parameter using `=`.
# 2. If no value is passed, the default is used. If a value is passed, it overrides the default.
# 3. Rule: Default arguments must come AFTER non-default arguments.

# Example:
def greet_user(name, message="Welcome!"):
    print(f"Hello {name}, {message}")

# Calling using the default value for 'message'
greet_user("Alice")

# Calling and overriding the default 'message'
greet_user("Bob", "Good morning!")







# ------------------ Keyword Arguments in Python ------------------
# Theory:
# 1. You can pass arguments to a function using the parameter names (key=value).
# 2. When using keyword arguments, the order in which you pass them doesn't matter.
# 3. Rule: In a function call, positional arguments must come before keyword arguments.

# Example:
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Calling with keyword arguments (order can be changed)
display_info(age=25, name="Alice")

# Calling with both (positional must come first)
display_info("Bob", age=30)





# ------------------ *args and **kwargs in Python ------------------
# Theory:
# 1. *args allows a function to accept any number of positional arguments (stored as a tuple).
# 2. **kwargs allows a function to accept any number of keyword arguments (stored as a dictionary).
# 3. Rule for ordering: standard arguments, *args, default arguments, **kwargs.

# Example 1: Using only *args
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4)) # Output: 10


# Example 2: Using only **kwargs
def print_user_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_details(name="Alice", age=25) 
# Output: name: Alice \n age: 25


# Example 3: Combined together
def student_info(*args, **kwargs):
    print("Positional (*args):", args)
    print("Keyword (**kwargs):", kwargs)

# Passing multiple positional and keyword arguments
student_info('Math', 'Art', name='John', age=22)
# Output:
# Positional (*args): ('Math', 'Art')
# Keyword (**kwargs): {'name': 'John', 'age': 22}

