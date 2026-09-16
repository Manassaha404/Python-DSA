# Abstract Class 
# Theory:
# An abstract class is a class that cannot be instantiated directly it's meant only to be inherited from. 
# It can define abstract methods (declared but with no implementation) that every child class is forced to override. 
# It's used to enforce a common interface/contract across subclasses. 
# In Python, this is done using the abc module (ABC and @abstractmethod).

from abc import ABC, abstractmethod 

# Defining an abstract class 
class Shape(ABC):                    # inherits from ABC -> makes it abstract
    @abstractmethod
    def area(self):                  # abstract method -> no implementation here
        pass                         # subclasses MUST override this

# Cannot instantiate an abstract class directly 

# s = Shape()   # TypeError: Can't instantiate abstract class Shape
#               # with abstract method area 

# Child class MUST implement the abstract method 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                  # required override
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):                  # required override
        return self.side ** 2

c = Circle(5)
sq = Square(4)
print(c.area())    # 78.5
print(sq.area())    # 16

# Forgetting to implement -> error at instantiation 

class Triangle(Shape):
    pass   # did NOT implement area()

# t = Triangle()   # TypeError: Can't instantiate abstract class Triangle
#                   # with abstract method area