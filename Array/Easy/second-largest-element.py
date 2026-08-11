# find the second largest element 
# 56,7,45,99,34,5,6 -> 56 

# Time Complexity  : O(n) — single pass through the array tracking largest and second largest
# Space Complexity : O(1) — only two variables used, no extra space proportional to input
def secLargest(arr:list[int]):
    if len(arr) == 0:
        return -1
    largest = arr[0]
    second_largest = -2**31 
    for element in arr:
        if element > largest:
            second_largest = largest
            largest = element
    return second_largest

a = [7,7,7,7,7,7] 
print(secLargest(a))




