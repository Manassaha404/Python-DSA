# Class Variables 


# Theory:
# A class variable is a variable defined directly inside the class body (not inside __init__ or any method),
# and it's shared by all instances of that class. 
# Unlike instance variables (which are unique per object and usually set via self.x = ...), 
# class variables live on the class itself. There is only one copy of a class variable, 
# no matter how many objects you create — so if it's mutated through the class, the change is visible to every instance.

# Defining a class variable 

class Employee:
    # class variable -> defined outside __init__, shared by ALL instances
    company_name = "TechCorp"
    raise_percent = 1.05   # another class variable

    def __init__(self, name, salary):
        self.name = name       # instance variable -> unique per object
        self.salary = salary   # instance variable -> unique per object

# Accessing class variables via class or instance

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.company_name)     # TechCorp -> accessed via instance
print(emp2.company_name)     # TechCorp -> same value, shared
print(Employee.company_name) # TechCorp -> accessed directly via class 

# Class variable is SHARED -> changing it via the class affects all instances 
Employee.company_name = "NewTech" 
print(emp1.company_name)     # NewTech -> changed for emp1 too
print(emp2.company_name)     # NewTech -> changed for emp2 too 

# assigning via an instance creates a NEW
# instance variable, it does NOT modify the class variable

emp1.company_name = "Alice's Own Company"

print(emp1.company_name)     # Alice's Own Company -> instance variable (new, shadows class var)
print(emp2.company_name)     # NewTech -> unaffected, still using class variable
print(Employee.company_name) # NewTech -> class variable itself unchanged 


