#  Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

# Time Complexity: O(N + M) where N = len(nums2) and M = len(nums1)
# Space Complexity: O(N) for the monotonic stack and hash map
def nextGreaterElement( nums1: list[int], nums2: list[int]) -> list[int]:
    resultMap = {}
    n = len(nums2)
    stack = []
    for i in range(n - 1, -1, -1):
        el = nums2[i]
        if len(stack) > 0 and stack[len(stack) - 1] > el:
            resultMap[el] = stack[len(stack) - 1]
        elif len(stack) > 0 and stack[len(stack) - 1] <= el:
            while len(stack) > 0 and stack[len(stack) - 1] <= el:
                stack.pop()
            if len(stack) > 0 and stack[len(stack) - 1] > el:
                resultMap[el] = stack[len(stack) - 1]
            else:
                resultMap[el] = -1
        else:
            resultMap[el] = -1
        stack.append(el)
    for i in range(len(nums1)):
        nums1[i] = resultMap[nums1[i]]
    return nums1

print(nextGreaterElement([1,2], [1,2,3,4]))