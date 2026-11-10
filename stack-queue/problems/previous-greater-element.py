# Previous Greater Element

# Time Complexity: O(N) - each element is pushed and popped from the stack at most once
# Space Complexity: O(N) - for the result array and monotonic stack (worst case all elements in stack)
def prevGreater(arr):
    # result = [-1] * len(arr)
    # stack = []
    # for i in range(len(arr)):
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
    for i in range(n):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

print(prevGreater([8, 8, 2, 2, 4, 9, 1, 1, 5, 10]))
# [-1, -1, 8, 8, 8, -1, 9, 9, 9, -1]