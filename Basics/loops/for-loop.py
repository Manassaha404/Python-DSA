# for loop -> repeats a block of code a specific number of times
# range() -> generates a sequence of numbers, which is used to control the number of iterations
# for i in range(start, stop, step):


for i in range(5):  # iterates from 0 to 4 (5 times)
    print(f"Iteration {i + 1}: Hello, World!")  # prints "Hello, World!" 5 times
  
  
    
for i in range(1, 101):
    if i % 2 == 0:  # checks if the number is even
        print(f"{i} is even")  # prints the even number
    else:
        print(f"{i} is odd")  # prints the odd number


