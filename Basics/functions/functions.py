 
# Theory: What is a Function in Python?
# 1. A function is a block of organized, reusable code that is used to perform a specific task.
# 2. Functions help break our program into smaller, modular chunks. As our program grows larger, functions make it more organized and manageable.
# 3. They avoid repetition and make the code reusable.
# 
# Key Components of a Function:
# - `def` keyword: This tells Python that you are defining a new function.
# - Function Name: An identifier to call the function later (e.g., `calculate_sum`). Follows the same naming rules as variables (lowercase with underscores is the convention).
# - Parameters (Arguments): The values you pass into the function so it can use them. These go inside parentheses `()`. They are optional.
# - Colon `:` : Marks the end of the function header and the start of the function body.
# - Function Body: The indented block of code that executes when the function is called.
# - `return` statement: (Optional) Used to send a computed result back to the caller. If omitted, the function implicitly returns `None`.

# Example: Creating and using a function


# Defining the function
def add_numbers(num1, num2):
    # - 'def' is the keyword indicating a function definition.
    # - 'add_numbers' is the name of our function.
    # - 'num1' and 'num2' are the parameters (inputs expected by the function).
    
    # Function body starts here (must be indented)
    sum_result = num1 + num2

    # 'return' sends the value of sum_result back to where the function was called.
    # Once 'return' is executed, the function immediately exits.
    return sum_result

# Calling (invoking) the function
# We use the function name followed by parentheses containing the actual values (arguments) we want to pass.
# Here, 5 is passed to 'num1' and 10 is passed to 'num2'.
final_answer = add_numbers(5, 10) 

# Using the result
# The returned value (15) was stored in the variable 'final_answer', which we can now print.
print(f"The sum is: {final_answer}")

