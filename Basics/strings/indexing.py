# indexing = accessing elements of a sequence using [] (index operator)
# [start:stop:step] -> returns a slice of the sequence from start index to stop index (exclusive) with a step size of step

credit_card_number = "1234-5678-9012-3456"

# Accessing individual characters using indexing
print(credit_card_number[4]) # prints the character at index 4 (5th character) -> '-'

# prints the characters from index 0 to 3 (4th character) -> '1234'
print(credit_card_number[0:4]) 



# prints the characters from index 5 to last character (5th character to last) -> '5678-9012-3456'
print(credit_card_number[5:])

# prints the last character of the string -> '6'
print(credit_card_number[-1])


# prints the characters from index 0 to 14 (15th character) with a step size of 2
print(credit_card_number[0:15:2])



# slicing the last four digits of the credit card number
last_four_digits = credit_card_number[-4:] 
print(f"our credit card number is: XXXX-XXXX-XXXX-{last_four_digits}")

# reverses the string
reverse_string = credit_card_number[-1:0:-1] 
print(f"The reversed credit card number is: {reverse_string}")
