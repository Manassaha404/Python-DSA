# four sum 
# [1,0,-1,0,-2,2], target = 0 
# -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# https://leetcode.com/problems/4sum/description/
def fourSum(nums: list[int], target: int) -> list[list[int]]:
    # Time Complexity: O(N^3), where N is the length of nums. Sorting takes O(N log N) and the nested loops take O(N^3).
    # Space Complexity: O(1) auxiliary space, ignoring the space required for the output list and sorting.
    nums.sort() 
    result = [] 
    n = len(nums) 
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue 
        for j in range(i+1, n):
            if j != (i + 1) and nums[j] == nums[j-1]:
                continue 
            k = j + 1
            l = n - 1
            while k < l:
                sum = nums[i] + nums[j] + nums[k] + nums[l] 
                if sum == target:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1 
                    l -= 1
                    while k < l and nums[k] == nums[k-1]:
                        k += 1 
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1 
                elif sum > target:
                    l -= 1
                else:
                    k += 1
    return result

print(fourSum([1,0,-1,0,-2,2], 0))