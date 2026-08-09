# palindrome number 
# 121 -> 121 (after reverse) so it is palindrome 

def isPalindrome(x:int):
    number = x
    if x < 0: 
        return False
    rev_number = 0
    while x > 0:
        rev_number = (rev_number * 10) + (x % 10)
        x //= 10
    print(rev_number)
    if rev_number == number:
        return True
    return False

print(isPalindrome(121))