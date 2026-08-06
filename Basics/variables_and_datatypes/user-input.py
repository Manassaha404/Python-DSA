# input() = function that allows user input returns a string data type

name = input("Enter your name: ")
age = input("Enter your age: ")
print(type(name)) # <class 'str'>
print(type(age)) # <class 'str'>
print(f"Hello {name}, you are {age} years old.")