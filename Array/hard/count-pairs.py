# count pairs where nums[i] > nums[j] and j > i 
# [5,3,4,1,2] -> [5,3] [5,4] [5,1] [5,2] [3,1] [3,2] [4,1] [4,2] -> 8 
# Time Complexity: O(N log N)
# Space Complexity: O(N)


def merge(nums:list[int], low:int, mid:int, high:int, count):
    temp = [] 
    left = low 
    right = mid + 1
    while left <= mid and right <= high:
        if nums[left] > nums[right]:
            temp.append(nums[right]) 
            right += 1 
            count["count"] += (mid - left + 1) 
        else:
            temp.append(nums[left])
            left += 1 
    while left <= mid:
        temp.append(nums[left])
        left += 1 
    while right <= high:
        temp.append(nums[right])
        right += 1 
    for i in range(low, high + 1):
        nums[i] = temp[i - low] 


def mergeSort(nums:list[int], low:int, high:int, count): 
    if low >= high:
        return 
    mid = low + (high - low) // 2
    mergeSort(nums, low, mid, count)
    mergeSort(nums, mid + 1, high,count) 
    merge(nums, low, mid, high, count)  


def countPairs(nums:list[int]):
    low = 0
    high = len(nums) - 1
    count = {"count" : 0} 
    mergeSort(nums, low, high, count)  
    return count["count"] 

nums = [5,3,4,2,1] 
print(countPairs(nums))  
print(nums) 