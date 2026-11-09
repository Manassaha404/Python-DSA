# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

# Time Complexity: O(N) where N is the length of string s
# Space Complexity: O(N) for the stack storing open brackets
def isValid(s: str) -> bool:
    openStack = []
    p = ["{", "(", "["]
    d = {"}": "{", ")": "(", "]": "["}
    for i in s:
        if i in p:
            openStack.append(i)
        else:
            if len(openStack) < 1:
                return False
            lastOpening = openStack.pop()
            if d[i] != lastOpening:
                return False
    if len(openStack) > 0:
        return False
    return True