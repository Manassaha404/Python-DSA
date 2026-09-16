# Objects in Python 


# Theory:
# An object is an instance of a class a bundled unit of data (attributes) and behavior (methods).
# In Python, literally everything is an object: integers, strings, functions, classes themselves.
# Every object has three key traits: identity (a unique id, i.e. its memory address, accessible via id()),
# type (what class it belongs to, accessible via type()), and value (the data it holds).
# Creating an object from a class is called instantiation.

x = 10
print(type(x))     # <class 'int'>  -> x is an object of class int
print(id(x))        # unique identity (memory address) of this object

s = "hello"
print(type(s))      # <class 'str'> -> strings are objects too


# Defining a class = blueprint for creating objects 
class Dog:
    # class-level attribute (shared by all objects of this class)
    species = "Canis familiaris"

    # __init__ runs automatically when an object is created (constructor)
    def __init__(self, name, age):
        self.name = name    # instance attribute (unique to each object)
        self.age = age      # instance attribute

    # instance method -> behavior of the object
    def bark(self):
        print(f"{self.name} says Woof!") 

# Instantiation -> creating objects from the class 

dog1 = Dog("Rex", 3)    # dog1 is an OBJECT (instance) of class Dog
dog2 = Dog("Bella", 5)  # dog2 is another, separate OBJECT of class Dog

dog1.bark()   # Rex says Woof!
dog2.bark()   # Bella says Woof! 

# Each object has its own identity, type, and value
print(type(dog1))     # <class '__main__.Dog'>
print(type(dog2))     # <class '__main__.Dog'>
print(id(dog1))        # unique id for dog1
print(id(dog2))        # different id -> separate object in memory

print(dog1 is dog2)    # False -> different objects, even though same class 
print(dog1.name, dog2.name)   # "Rex Bella" -> different values/state 


# Objects hold both data (attributes) and behavior (methods)

print(dog1.name)      # accessing attribute (data)
dog1.bark()             # calling method (behavior) 




