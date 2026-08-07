# dictionary -> A mutable, unordered collection of {key-value} pairs. 
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be of any data type and can be duplicated.

# ------- creating a dictionary using {} -------
person = {
    "name": "Alice",
    "age": 28,
    "city": "New York",
    "is_student": False
}
print("Original Dictionary:", person)


# ------- Accessing Elements -------
# Using bracket notation [] (Throws KeyError if key doesn't exist)
print("Name:", person["name"])
# Using get() method (Returns None or a default value if key doesn't exist)
print("Age:", person.get("age"))
print("Country (not in dict):", person.get("country", "Default Country"))


# ------- Adding and Updating Elements ------- 
# Adding a new key-value pair
person["job"] = "Engineer"
# Updating an existing key's value
person["age"] = 29
print("After Add/Update:", person)

# update() method -> Updates dictionary with elements from another dictionary or iterable of key/value pairs
person.update({"city": "San Francisco", "hobby": "Reading"})
print("After update():", person)


# ------- Dictionary Methods -------
# keys() -> Returns a view object containing the dictionary's keys
print("Keys:", person.keys())

# values() -> Returns a view object containing the dictionary's values
print("Values:", person.values())

# items() -> Returns a view object containing tuples of (key, value) pairs
print("Items:", person.items())

# setdefault() -> Returns the value of a key. If key doesn't exist, inserts the key with a specified value.
hobby = person.setdefault("hobby", "Unknown") # 'hobby' exists, returns 'Reading'
salary = person.setdefault("salary", 100000)  # 'salary' doesn't exist, adds it.
print("After setdefault():", person)

# pop() -> Removes the specified key and returns its value
removed_job = person.pop("job")
print(f"Removed '{removed_job}' using pop('job'). Dict now:", person)

# popitem() -> Removes and returns the last inserted key-value pair as a tuple (in Python 3.7+)
last_item = person.popitem()
print(f"Removed {last_item} using popitem(). Dict now:", person)


# ------- Iterating Through a Dictionary ------- 
# Iterating over keys (Default behavior)
print("Iterating over keys:")
for k in person:
    print(k, end=" | ")
print()

# Iterating over items (key, value pairs)
print("Iterating over items:")
for key, value in person.items():
    print(f"{key}: {value}")


# ------- Copying and Clearing -------
# copy() -> Returns a shallow copy of the dictionary
person_copy = person.copy()

# clear() -> Removes all elements from the dictionary
person_copy.clear()
print("Original person dict:", person)
print("Cleared copy dict:", person_copy)


