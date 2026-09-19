# find factorial of n 
# n! = n * (n - 1) * (n - 2) * (n - 3) * . . . 
# 1! = 1 
# 0! = 1 

def fact(n:int) -> int:
    if n <= 1:
        return 1 
    return n * fact(n - 1) 

# Time Complexity: O(n)  - n recursive calls are made (from n down to 1)
# Space Complexity: O(n) - O(n) call stack frames are held simultaneously

print(fact(5))