# Subsets 
# https://leetcode.com/problems/subsets/description/
def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    n = len(nums)
    def helper(set:list[int], i:int):
        nonlocal result
        nonlocal n
        nonlocal nums
        result.append(set)
        i = i + 1
        while i < n:
            helper(set + [nums[i]], i)
            i += 1
    helper([], -1)
    return result

# Time Complexity: O(n * 2^n) - there are 2^n total subsets, and copying each subset takes O(n) time
# Space Complexity: O(n) - auxiliary space for recursion call stack of depth at most n (or O(n * 2^n) if output list is included)

print(subsets([1, 2, 3]))

