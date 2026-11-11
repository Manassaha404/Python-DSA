# Sum of Subarray Ranges
# https://leetcode.com/problems/sum-of-subarray-ranges/description/

# Time Complexity: O(N) - nextGreater, prevGreater, prevSmaller, and nextSmaller each run in O(N)
#                  using a monotonic stack; the contribution loops run in O(N), giving overall O(N)
# Space Complexity: O(N) - for the monotonic stacks and the auxiliary arrays (prevG, nextG, prevS, nextS)
def subArrayRanges(nums: list[int]) -> int:
    def sumOfSubArrayMax(arr):
        def nextGreater(arr):
            stack = []
            n = len(arr)
            result = [n] * n
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()
                if stack:
                    result[i] = stack[-1]
                stack.append(i)
            return result

        def prevGreater(arr):
            stack = []
            n = len(arr)
            result = [-1] * n
            for i in range(n):
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                if stack:
                    result[i] = stack[-1]
                stack.append(i)
            return result

        total = 0
        prevG = prevGreater(arr)
        nextG = nextGreater(arr)
        for i in range(len(arr)):
            contribution = (i - prevG[i]) * (nextG[i] - i)
            total += (arr[i] * contribution)
        return total

    def sumOfSubArrayMin(arr):
        def prevSmaller(arr):
            stack = []
            n = len(arr)
            result = [-1] * n
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    result[i] = stack[-1]
                stack.append(i)
            return result

        def nextSmaller(arr):
            stack = []
            n = len(arr)
            result = [n] * n
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                if stack:
                    result[i] = stack[-1]
                stack.append(i)
            return result

        total = 0
        prevS = prevSmaller(arr)
        nextS = nextSmaller(arr)
        for i in range(len(arr)):
            contribution = (i - prevS[i]) * (nextS[i] - i)
            total += (arr[i] * contribution)
        return total

    return sumOfSubArrayMax(nums) - sumOfSubArrayMin(nums)