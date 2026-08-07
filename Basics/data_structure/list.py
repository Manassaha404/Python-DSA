#collection -> a single variable that can hold multiple values
#list[] -> a collection of values that are ordered and changeable. Allows duplicate members.

fruits = ["apple", "banana", "cherry"]  # a list of fruits
print(fruits)  # output: ['apple', 'banana', 'cherry']

print(fruits[0])  # output: apple (accessing the first element of the list)
print(fruits[1])  # output: banana (accessing the second element of the list)
print(fruits[2])  # output: cherry (accessing the third element of the list)

print(fruits[-1])  # output: cherry (accessing the last element of the list)
# print(fruits[4]) ->  # output: IndexError: list index out of range (trying to access an index that doesn't exist in the list)

# list is iterable -> can be looped through using a for loop
for fruit in fruits:  # iterating through the list of fruits
    print(fruit)  # prints each fruit in the list

#list methods -> built-in functions that can be used to manipulate lists
fruits.append("orange")  # adds "orange" to the end of the list
print(fruits)  # output: ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "kiwi")  # inserts "kiwi" at index 1
print(fruits)  # output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']

fruits.remove("banana")  # removes "banana" from the list
print(fruits)  # output: ['apple', 'kiwi', 'cherry', 'orange']

fruits.pop()  # removes the last element from the list
print(fruits)  # output: ['apple', 'kiwi', 'cherry']

fruits.sort()  # sorts the list in ascending order
print(fruits)  # output: ['apple', 'cherry', 'kiwi']

fruits.reverse()  # reverses the order of the list
print(fruits)  # output: ['kiwi', 'cherry', 'apple']


new_fruits = fruits.copy()  # creates a copy of the list
print(new_fruits)  # output: ['kiwi', 'cherry', 'apple']

fruits.clear()  # removes all elements from the list
print(fruits)  # output: []

print(len(new_fruits))  # output: 3 (returns the number of elements in the list)

kiwi_index = new_fruits.index("kiwi")  # gets the index of "kiwi" in the list
print(kiwi_index)  # output: 0 (the index of "kiwi" in the list)

count_cherry = new_fruits.count("cherry")  # counts how many times "cherry" appears in the list
print(count_cherry)  # output: 1 (the number of times "cherry" appears in the list)
