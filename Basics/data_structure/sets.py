# collection -> a single variable that can hold multiple values
# set{} -> a collection of values that are unordered, unchangeable (but can be added to), and do not allow duplicate members.

fruits = {"apple", "banana", "cherry"}  # a set of fruits
print(fruits)  # output: {'banana', 'cherry', 'apple'} (the order may vary since sets are unordered)


# add into a sets 
fruits.add("pineapple") 
print(fruits) # {'banana', 'cherry', 'apple', 'pineapple'} 

fruits.add("pineapple") # still {'apple', 'pineapple', 'cherry', 'banana'} -> sets remove duplicate values


# sets are iterable 
for fruit in fruits:
    print(fruit)


