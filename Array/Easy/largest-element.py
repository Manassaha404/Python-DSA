# Find the largest element -> 
# 56,7,45,99,34,5,6 -> 99 

# Time Complexity  : O(n) — single pass through the array
# Space Complexity : O(1) — only one variable `ans` used, no extra space
def largest(arr:list[int]):
    if len(arr) == 0:
        return -1
    ans = arr[0]
    for element in arr:
        if element > ans:
            ans = element
    return ans;

a = [56,7,45,99,34,5,6]
print(largest(a))
