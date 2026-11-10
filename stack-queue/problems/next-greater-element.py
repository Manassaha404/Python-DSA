#  Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

# Time Complexity: O(N) - each element is pushed and popped from the stack at most once
# Space Complexity: O(N) - for the result array and monotonic stack (worst case all elements in stack)
def nextGreater(arr):
    # n = len(arr)
    # result = [-1] * n
    # stack = []
    # for i in range(n - 1, -1, -1):
    #     if stack == []:
    #         result[i] = -1
    #     elif arr[i] >= stack[-1]:
    #         while (len(stack) > 0 and stack[-1] <= arr[i]):
    #             stack.pop()
    #         if len(stack) > 0:
    #             result[i] = stack[-1]
    #         else:
    #             result[i] = -1
    #     else:
    #         result[i] = stack[-1]
    #     stack.append(arr[i])
    # return result
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

# Time Complexity: O(N + M) - O(N) for nextGreater on nums2 + O(N) to build map + O(M) for nums1 lookup
#                  where N = len(nums2), M = len(nums1)
# Space Complexity: O(N) - for the hash map storing next greater values of nums2
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    nextG = nextGreater(nums2)
    resultMap = {}
    for i in range(len(nums2)):
        resultMap[nums2[i]] = nextG[i]
    for i in range(len(nums1)):
        nums1[i] = resultMap[nums1[i]]
    return nums1
print(nextGreaterElement([1,2], [1,2,3,4]))