# find repeating and missing number 
# [1,4,5,3,1,6] -> [missing, repeating] -> [2,1] 
# number in array always 1 to n 
# Time Complexity: O(N)
# Space Complexity: O(1)
def findRepeatingAndMissing(nums:list[int]):
    n = len(nums) 
    sum = 0
    sum2 = 0
    sumN = (n*(n + 1)) / 2 
    sum2N = (n*(n+1)*(2 * n + 1)) / 6 
    for num in nums:
        sum += num 
        sum2 += num**2 
    repeating = ((sumN - sum) + ((sum2N - sum2)/(sumN - sum))) / 2
    missing = repeating - sumN + sum 
    return {int(repeating), int(missing)} 

print(findRepeatingAndMissing([1,4,5,3,1,6]))

    
    
