# extraction of digits 
# 5684 -> 5,6,8,4 

def extractionOfDigits(n):
    digits = []
    while n > 0:
        digit = n % 10 
        digits.append(digit)
        n //= 10
    return digits


digits = extractionOfDigits(64787)
print(digits)



# count of digits 
# 64736 -> 5
def countOfDigits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


import math
def countOfDigitsByLog(n):
    result = int(math.log10(n) + 1)
    return result

print(countOfDigits(6473676756576565))       # -> 16
print(countOfDigitsByLog(6473676756576565))  # -> 16


# Time Complexity = O(log10(n)) 


