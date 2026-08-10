# character hashing -> 
# Problem: "hdusahdh" check the occurrence of each individual character of the string. 
# in this problem we need hashing 
#
# Theory:
# 1. Hashing is a technique used to pre-store and fetch data efficiently in O(1) time.
# 2. For character hashing, we can use a frequency array (or a hash map) to store the occurrences of each character.
# 3. If the string contains only lowercase English letters ('a' - 'z'), we can use an array of size 26.
#    - The index for a character 'c' can be calculated as: ord(c) - ord('a')
#    - For example, 'a' maps to index 0, 'b' to 1, ..., 'z' to 25.
# 4. If the string contains any ASCII character, we can use an array of size 256.
#    - The index will simply be the ASCII value of the character: ord(c)
# 5. Algorithm:
#    - Initialize a hash array of the required size (e.g., 26 or 256) with zeros.
#    - Iterate through each character in the string.
#    - For each character, compute its index and increment the value at that index in the hash array.
#    - To check the occurrence of any character later, simply look up its computed index in the array.


def hashOverString(str:str):
    hashMap = [0] * 256
    for char in str:
        index = int(ord(char) - ord('a'))
        hashMap[index] += 1
    return hashMap

def checkOccurrenceOfEachCharInString(str:str):
    hashMap = hashOverString(str)
    result = {}
    for char in str:
        index = int(ord(char) - ord('a'))
        result[char] = hashMap[index]
    return result


print(checkOccurrenceOfEachCharInString("Manas saha"))
#time complexity -> O(n) 
