# Count Operations to Obtain Zero 


# You are given two non-negative integers num1 and num2.
# In one operation, if num1 >= num2, you must subtract num2 from num1, 
# otherwise subtract num1 from num2.

# Input: num1 = 2, num2 = 3
# Output: 3
# Explanation: 
# - Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
# - Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
# - Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
# Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
# So the total number of operations required is 3.

# https://leetcode.com/problems/count-operations-to-obtain-zero/description/ 
def countOperations(num1: int, num2: int) -> int:
    def helper(num1:int, num2:int, count = 0):
        if num1 == 0 or num2 == 0:
            return count  
        if num1 >= num2:
            count += num1 // num2 
            return helper(num1 % num2, num2, count) 
        else:
            count += num2 // num1
            return helper(num1, num2 % num1, count) 
    return helper(num1, num2)

# Time Complexity: O(log(min(num1, num2))) - similar to Euclidean GCD; each step reduces
#                                            the larger number significantly via floor division
# Space Complexity: O(log(min(num1, num2))) - recursion depth follows the same reduction pattern

print(countOperations(2,3)) 

