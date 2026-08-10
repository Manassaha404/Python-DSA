# number list hashing -> 
# 
# Theory:
# 1. Hashing for a list of numbers allows us to pre-store the frequency of each number to fetch them later in O(1) time.
# 2. Array-based Hashing (Frequency Array): 
#    - We create a "hash array" where the index of the array represents the number itself.
#    - The size of this hash array must be at least `maximum_element_in_the_list + 1`.
# 3. Algorithm:
#    - Initialize a hash array of the required size with all zeros.
#    - Iterate through the given list of numbers.
#    - For each number `x`, increment the value at index `x` in the hash array: hash[x] += 1
#    - To find how many times a number `q` appears, we simply look up hash[q].
# 4. Limitations of Array-based Hashing:
#    - It requires the numbers to be non-negative.
#    - It consumes a lot of memory if the maximum number is very large (e.g., 10^9). Creating an array of size 10^9 is generally not feasible due to memory limits (typically 10^7 is the max size for global arrays in C++, but in Python it can still be inefficient).
# 5. Alternative (Hash Maps / Dictionaries):
#    - When dealing with large or negative numbers, it is better to use a hash map (like Python's `dict` or `collections.Counter`).
#    - Hash maps only allocate memory for elements that actually exist in the list.


def numberHashing(nums:list[int]):
    hashMap = {}
    for num in nums:
        key = num
        if hashMap.get(key):
            hashMap[key] += 1
        else:
            hashMap[key] = 1
    return hashMap


hash = numberHashing([6,6,6,6,6,6,6,6,6,6,6,6,56,5,4,54,3,434,4,4,3432,432,65,6546,6544])
print(hash)          
