# most frequent even number 
# [0,1,2,2,4,4,1] -> 2 
# https://leetcode.com/problems/most-frequent-even-element/description/
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(N) to store even numbers in hash map
def mostFrequentEven(nums:list[int]):
    hashMap = {}
    for num in nums:
        if num % 2 == 0:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
    if not hashMap:
        return -1
    evenNumbers = list(hashMap.keys())
    most_frequent = evenNumbers[0]
    for num in evenNumbers:
        if hashMap[most_frequent] < hashMap[num]:
            most_frequent = num 
        if hashMap[most_frequent] == hashMap[num]:
            if num < most_frequent:
                most_frequent = num    
    return most_frequent

print(mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))
