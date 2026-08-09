# reverse a number 
# 54673 -> 37645 
# https://leetcode.com/problems/reverse-integer/description/


def reverseNumber(x:int):
    n = abs(x)
    
    number = 0

    while n > 0:
        number = (number * 10) + (n % 10)
        n //= 10
    if number.bit_length() >= 32:
        return 0
    if x < 0:
        return -number
    else:
        return number
print(reverseNumber(1563847412))
