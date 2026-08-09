# armstrong number 
# 1634 = 1^4 + 6^4 + 3^4 + 4^4 -> it means it is a armstrong number 
# 153 = 1^3 + 5^3 + 3^3 
import math
def isArmstrong(n:int):
    actual_number = n
    count = int(math.log10(n) + 1)
    num = 0
    while n > 0:
        digit = n % 10 
        num += digit**count
        n //= 10
    if num == actual_number:
        return True
    else: 
        return False

print(isArmstrong(1634))
print(isArmstrong(153))