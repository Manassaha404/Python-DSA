# while loop -> repeats a block of code as long as a condition is true
name = input("What is your name? ")

# this while loop will keep asking the user for their name until they enter a non-empty string
while name == "":
    print("You didn't enter a name. Please try again.")
    name = input("What is your name? ")
print(f"Hello, {name}!")


age = int(input("How old are you? "))
while age < 0:
    print("Age cannot be negative. Please enter a valid age.")
    age = int(input("How old are you? "))
print(f"You are {age} years old.")