# find missing numbers -> 
# https://leetcode.com/problems/find-missing-elements/description/
# [1,4,2,5] -> [3] 
def findMissingElements(nums:list[int]):
    nums.sort()
    result = []
    smallest = nums[0]
    largest = nums[len(nums) - 1]
    i = 1
    while smallest < largest - 1:
        if smallest + 1 != nums[i]:
            result.append(smallest + 1)
            smallest += 1
        else:
            i += 1
            smallest += 1
    return result

# Time Complexity: O(n log n) - dominated by the sort; the while loop is O(largest - smallest) ≈ O(n)
# Space Complexity: O(k) - where k is the number of missing elements stored in result;
#                          O(log n) extra for the in-place sort (call stack)

print(findMissingElements([1,4,2,5]))
    


