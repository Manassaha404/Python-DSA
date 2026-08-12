# find the number of max consecutive ones from a binary array 
# [1,0,1,1,0,1] -> 2 



def findMaxConsecutiveOnes(nums:list[int]):
    pre_max_count = 0
    current_count = 0
    for element in nums:
        if element == 1:
            current_count += 1
        else:
            if current_count >= pre_max_count:
                pre_max_count = current_count
            current_count = 0
    return max(current_count,pre_max_count) 

# Time Complexity: O(n) - single pass through the array
# Space Complexity: O(1) - only two counter variables used

print(findMaxConsecutiveOnes([1,0,1,1,0,1]))
