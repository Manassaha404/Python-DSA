# reverse pairs 
# nums = [1,3,2,3,1] -> 
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# -> 2 
# Time Complexity: O(N log N)
# Space Complexity: O(N)



# https://leetcode.com/problems/reverse-pairs/description/
def merge(nums:list[int], low:int, mid:int, high:int, count):
        left = low 
        right = mid + 1 
        while left <= mid and right <= high:
            if nums[left] > nums[right] * 2:
                count["count"] += (mid - left + 1) 
                right += 1 
            else:
                left += 1 
        left = low 
        right = mid + 1
        temp = [] 
        while left <= mid and right <= high:
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left += 1 
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1 
        while right <= high:
            temp.append(nums[right])
            right += 1 
        for i in range(low, high + 1):
            nums[i] = temp[i - low] 
        


def mergeSort( nums:list[int], low:int, high:int, count):
    if low >= high:
        return 
    mid = low + (high - low) // 2
    mergeSort(nums, low, mid, count)
    mergeSort(nums, mid + 1, high, count) 
    merge(nums, low, mid, high, count)


def reversePairs( nums: list[int]) -> int:
    low = 0 
    high = len(nums) - 1
    count = {"count": 0}
    mergeSort(nums, low, high, count)  
    return count["count"] 


nums = [2,4,3,5,1] 
print(reversePairs(nums)) 