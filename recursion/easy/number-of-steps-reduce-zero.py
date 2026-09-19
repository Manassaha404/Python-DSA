# Number of Steps to Reduce a Number to Zero 
# Input: num = 14
# Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
def numberOfSteps(num: int) -> int: 
    def helper(num:int, count = 0) -> int:
        if num <= 0:
            return count 
        count += 1
        if num % 2 == 0:
            return helper(num // 2, count)
        else:
            return helper(num - 1, count) 
    return helper(num, 0)

# Time Complexity: O(log n) - each even step halves num (dominant operation);
#                             odd steps only subtract 1 and are always followed by a halving
# Space Complexity: O(log n) - recursion depth is proportional to the number of bits in num

print(numberOfSteps(14))




