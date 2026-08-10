# https://leetcode.com/problems/first-unique-character-in-a-string/description/
def firstUniqChar(s:str) -> int:
    hashMap = [0] * 26
    for char in s:
        index = int(ord(char) - ord('a'))
        hashMap[index] += 1
    for char in s:
        hashMapIndex = int(ord(char) - ord('a'))
        if hashMap[hashMapIndex] == 1: 
            return s.index(char)
    return -1

print(firstUniqChar("aabb"))


