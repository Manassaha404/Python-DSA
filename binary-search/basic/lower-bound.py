# lower bound algorithm is used to find the index of the first element in a sorted array that is greater than or equal to the target value. If all elements are less than the target, it returns the length of the array.
# arr[j] >= target and arr[j-1] < target
# Time Complexity: O(log n)

# with ans variable 
# def lower_bound(arr: list[int], target: int) -> int:
#     left = 0 
#     right = len(arr) - 1 
#     ans = len(arr) 
#     while left <= right:
#         mid = left + (right - left) // 2 
#         if arr[mid] >= target:
#             ans = mid 
#             right = mid - 1 
#         else:
#             left = mid + 1 
#     return ans

def lower_bound(arr:list[int], target:int):
    low = 0 
    high = len(arr) - 1 
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] >= target:
            high = mid - 1 
        else:
            low = mid + 1 
    return low  

print(lower_bound([1], 1)) 
