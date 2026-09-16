# Inheritance 


# Theory:
# Inheritance lets a class (called the child/subclass/derived class) acquire the attributes and methods of another class 
# (called the parent/superclass/base class). 
# It models an "is-a" relationship (e.g. a Dog is an Animal) and promotes code reuse common behavior is written once 
# in the parent, and children can use it as-is, override it, or extend it. 
# Python supports single, multiple, multilevel, and hierarchical inheritance. 

# Basic inheritance -> child class inherits from parent 

class Animal:                       # parent / base class
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):                  # child class -> inherits from Animal
    pass                            # no new code, but gets everything from Animal


d = Dog("Rex")
d.eat()      # Rex is eating   -> inherited method
d.speak()    # Rex makes a sound -> inherited method
print(isinstance(d, Animal))  # True -> Dog IS-A Animal

# Overriding -> child provides its own version of a method 

class Cat(Animal):
    def speak(self):                # overrides Animal.speak()
        print(f"{self.name} says Meow!")

c = Cat("Whiskers")
c.eat()      # Whiskers is eating  -> inherited, unchanged
c.speak()    # Whiskers says Meow! -> overridden version used 



# Multilevel inheritance -> chain of classes  

class Puppy2(Dog):        # Puppy2 -> Dog -> Animal
    def play(self):
        print(f"{self.name} is playing")

pp = Puppy2("Max")
pp.eat()     # inherited from Animal (grandparent)
pp.speak()   # inherited from Animal, via Dog
pp.play()    # defined in Puppy2 itself

# Multiple inheritance -> child inherits from 2+ parents 

class Swimmer:
    def swim(self):
        print("Swimming...")

class Flyer:
    def fly(self):
        print("Flying...")

class Duck(Swimmer, Flyer):   # inherits from BOTH classes
    pass

duck = Duck()
duck.swim()   # Swimming...  -> from Swimmer
duck.fly()    # Flying...    -> from Flyer 





