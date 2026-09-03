# floor and ceil of a number in a sorted array
# floor is the largest element in the array that is less than or equal to the target value
# ceil is the smallest element in the array that is greater than or equal to the target value
# Time Complexity: O(log n)
# [5, 6, 7, 8, 9, 10] -> target = 7
# floor -> 7
# ceil -> 7
# [5, 6, 7, 8, 9, 10] -> target = 11
# floor -> 10
# ceil -> -1
def floor_ceil(arr: list[int], target: int) -> tuple[int, int]:
    left = 0 
    right = len(arr) - 1 
    floor = -1 
    ceil = -1 
    while left <= right:
        mid = left + (right - left) // 2 
        if arr[mid] == target:
            floor = arr[mid]
            ceil = arr[mid]
            return (floor, ceil)
        elif arr[mid] < target:
            floor = arr[mid]
            left = mid + 1 
        else:
            ceil = arr[mid]
            right = mid - 1 
    return (floor, ceil)