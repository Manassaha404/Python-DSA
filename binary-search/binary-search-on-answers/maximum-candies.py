# Maximum Candies Allocated to K Children 
# candies = [5,8,6], k = 3 
# -> 5 
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/ 

# Time Complexity : O(n) — iterates through all n candy piles once
# Space Complexity: O(1) — uses only a constant amount of extra space
def shouldChildren(candies, mid):
    ans = 0 
    if mid == 0:
        return ans 
    for candy in candies:
        ans += candy // mid
    return ans

# Time Complexity : O(n * log(max(candies)))
#   - Binary search runs O(log(max(candies))) iterations over [1, max(candies)]
#   - Each iteration calls shouldChildren which is O(n)
# Space Complexity: O(1) — only a few scalar variables used; no extra data structures
def maximumCandies(candies: list[int], k: int) -> int:
    sum_candies = sum(candies)
    if sum_candies < k:
        return 0 
    low = 1
    high = max(candies) 
    while low <= high:
        mid = low + (high - low) // 2 
        per_children = shouldChildren(candies, mid) 
        if per_children < k:
            high = mid - 1 
        else:
            low = mid + 1 
    return high 

print(maximumCandies([10,10,10,10,10], 5)) 
print(maximumCandies([1,2,3,4,10], 6)) 
print(maximumCandies([4,7,5], 4)) 