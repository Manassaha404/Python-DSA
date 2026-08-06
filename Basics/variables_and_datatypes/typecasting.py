# Typecasting = Converting one data type into another data type.
#                            str()  int()  float()  bool()

name = "Manas"
age = 25
cgpa = 5.6
height = 6.1
is_student = True

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(is_student)) # <class 'bool'>

cgpa = int(cgpa) # converting float to integer
print(cgpa) # 5

age = str(age) # converting integer to string
print(age) # 25
print(type(age)) # <class 'str'>


name = bool(name) # converting string to boolean
print(name) # True
empty_string = ""
empty_string = bool(empty_string) # converting empty string to boolean
print(empty_string) # False

