# Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/description/

# Time Complexity: O(N) where N is the length of nums (each element is pushed/popped at most twice)
# Space Complexity: O(N) for the monotonic stack
def nextGreaterElements(nums: list[int]) -> list[int]:
    stack = []
    n = len(nums)
    for i in range(n - 1, -1, -1):
        el = nums[i]
        if len(stack) > 0 and stack[-1] <= el:
            while len(stack) > 0 and stack[-1] <= el:
                stack.pop()
        stack.append(el)
    for i in range(n - 1, -1, -1):
        el = nums[i]
        if len(stack) > 0 and stack[-1] > el:
            nums[i] = stack[-1]
        elif len(stack) > 0 and stack[-1] <= el:
            while len(stack) > 0 and stack[-1] <= el:
                stack.pop()
            if len(stack) > 0 and stack[-1] > el:
                nums[i] = stack[-1]
            else:
                nums[i] = -1
        else:
            nums[i] = -1
        stack.append(el)
    return nums