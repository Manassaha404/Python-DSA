name = input("What is your name? ")



# len() -> returns the number of characters in a string
print(f"Your name has {len(name)} characters.")


# find() -> returns the index of the first occurrence of a substring in a string
find_letter = input("Enter a letter to find in your name: ")
first_occurrence = name.find(find_letter)
print(f"The first occurrence of '{find_letter}' in your name is at index: {first_occurrence}")


# count() -> returns the number of occurrences of a substring in a string
count_letter = input("Enter a letter to count in your name: ")
count = name.count(count_letter)
print(f"The letter '{count_letter}' appears {count} times in your name.")


# capitalize() -> returns a copy of the string with the first character capitalized and the rest lowercased
capitalized_name = name.capitalize()
print(f"Your name with the first letter capitalized: {capitalized_name}")

# upper() -> returns a copy of the string with all characters in uppercase
uppercased_name = name.upper()
print(f"Your name in uppercase: {uppercased_name}")

# lower() -> returns a copy of the string with all characters in lowercase
lowercased_name = name.lower()
print(f"Your name in lowercase: {lowercased_name}")

# isDigit() -> returns True if all characters in the string are digits, otherwise False
num = input("Enter a number: ")
is_digit = num.isdigit()
print(f"Is the number made up of digits only? {is_digit}")

# replace() -> returns a copy of the string with all occurrences of a substring replaced with another substring
old_substring = input("Enter a substring to replace in your name: ")
new_substring = input("Enter the new substring: ")
replaced_name = name.replace(old_substring, new_substring)
print(f"Your name after replacing '{old_substring}' with '{new_substring}': {replaced_name}")

