# https://leetcode.com/problems/rotate-array/description/
# -1,-100,3,99  k -> 2  -> 3,99,-1,-100 

# Time Complexity  : O(n) — three in-place reversal passes, each O(n) → overall O(n)
# Space Complexity : O(1) — all rotations done in-place using only a temp variable

# Helper: reverses a subarray in-place between indices start and end
def reverse(nums:list[int], start:int, end:int):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1

def rotate(nums:list[int], k:int):
    n = len(nums)
    k = n - (k % n) - 1
    reverse(nums, 0, k)
    reverse(nums, k + 1, n-1)
    reverse(nums, 0, n-1)




nums = [-1,-100,3,99]
rotate(nums, 2)
print(nums)
