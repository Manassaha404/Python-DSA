# logical operators are used to combine conditional statements 
#                           (and, or, not)
#                           and -> returns True if both statements are true
#                           or -> returns True if one of the statements is true
#                           not -> reverses the result, returns False if the result is true


temp = int(input("What is the temperature outside? "))
is_raining = input("Is it raining? (yes/no) ").lower() == "yes"

if temp > 35 or temp < 0 or is_raining:
    print("the plan is cancelled")
elif temp > 30 and not is_raining:
    print("the plan is on")
