# Remove K Digits
# https://leetcode.com/problems/remove-k-digits/description/

# Time Complexity: O(N) - each digit is pushed and popped from the stack at most once;
#                  slicing, stripping leading zeros, and joining take O(N)
#                  (Note: stack.pop(0) can take O(N^2) in worst case for list shifts)
# Space Complexity: O(N) - for the stack storing up to N digits and the output string
def removeKdigits(num: str, k: int) -> str:
    if len(num) == k:
        return "0"
    stack = []
    for ch in num:
        while k > 0 and stack and stack[-1] > ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    stack = stack[:len(stack) - k]
    while stack and stack[0] == '0':
        stack.pop(0)
    result = "".join(stack)
    if result == "":
        return "0"
    return result







print(removeKdigits("10200", 1))
