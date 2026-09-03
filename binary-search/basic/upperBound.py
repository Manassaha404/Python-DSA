# upper bound is the index of the first element in the array that is greater than the target value. If all elements are less than or equal to the target, it returns the length of the array.
# Time Complexity: O(log n)
# arr[j] > target and arr[j-1] <= target
def upper_bound(arr: list[int], target: int) -> int:
    left = 0 
    right = len(arr) - 1 
    ans = len(arr) 
    while left <= right:
        mid = left + (right - left) // 2 
        if arr[mid] > target:
            ans = mid 
            right = mid - 1 
        else:
            left = mid + 1 
    return ans