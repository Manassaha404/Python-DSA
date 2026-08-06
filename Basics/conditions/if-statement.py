# if = do some code if a condition is true
# else = do some code if the condition is false

age = int(input("How old are you? "))

# this is an if statement that checks if the age is greater than or equal to 18
if age >= 18:
    print("You are an adult.") #this code will run if the condition is true
else:
    print("You are a minor.") #this code will run if the condition is false
    
    
# elif = else if, checks another condition if the previous condition is false
if age < 0:
    print("You are not born yet.")
elif age == 0:
    print("You are a newborn.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")


for_sale = True
# this always a boolean value, so the if statement will always be true
if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")


# this is an if statement that checks if the user wants to buy an item
response = input("Do you want to buy this item? (yes/no) ")
if response.lower() == "yes":
    print("You have bought the item.")
elif response.lower() == "no":
    print("You have not bought the item.")