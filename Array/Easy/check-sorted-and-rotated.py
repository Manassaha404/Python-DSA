# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

# Time Complexity  : O(n) — two linear passes over the array (find pivot + validate rotated array)
# Space Complexity : O(n) — extra array `b` of size n to store the rotated sequence
def check(nums:list[int]):
    n = len(nums)
    pivotIndex = -1
    for i in range(1,n):
        if nums[i] < nums[i - 1]:
            pivotIndex = i 
            break
    if pivotIndex == -1:
        return True
    b = [0] * n 
    for i in range(n):
        b[i] = nums[(i+pivotIndex) % n]
    print(b)
    for i in range(1,n):
        if b[i] < b[i - 1]:
            return False
    return True 

a = [2,1,3,4]
print(check(a))


        
    


    
