# reverse number using recursion 
# 1234 -> 4321 
# https://leetcode.com/problems/reverse-integer/description/ 
import math 
def rev(n:int) -> int:
    if n == 0:
        digits = 1 
    else:
        digits = int(math.log10(abs(n))) + 1 
    def helper(n:int, digits:int) -> int:
        if digits <= 1:
            return n 
        return (n % 10) * (10 ** (digits - 1)) + helper(n // 10, digits - 1) 
    ans = helper(abs(n), digits)
    if 0 <= abs(ans) <= 2 ** 31 - 1:
        if n < 0:
            return -1 * ans 
        else:
            return ans 
    else:
        return 0 

# Time Complexity: O(d)  - where d = number of digits in n; helper recurses once per digit
# Space Complexity: O(d) - O(d) call stack frames, one per digit recursion depth

print(rev(1534236469))



 





