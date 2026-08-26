# max product sub array 
# [2,3,-2,4] -> [2,3] -> 6 
# https://leetcode.com/problems/maximum-product-subarray/description/ 
# Time Complexity: O(N)
# Space Complexity: O(1)

def maxProduct(nums: list[int]) -> int:
    suffix = 1 
    prefix = 1 
    max_prefix_product = float("-inf")
    max_suffix_product = float("-inf")
    n = len(nums) 
    for i in range(n):
        if prefix == 0:
            prefix = 1 
        if suffix == 0:
            suffix = 1 
        prefix *= nums[i] 
        suffix *= nums[n - 1 - i] 
        max_prefix_product = max(max_prefix_product, prefix) 
        max_suffix_product = max(max_suffix_product, suffix) 
    return max(max_prefix_product, max_suffix_product)

