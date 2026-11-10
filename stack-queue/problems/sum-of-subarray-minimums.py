# Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/description/

# Time Complexity: O(N) - prevSmaller and nextSmaller each run in O(N) using a monotonic stack;
#                  the final contribution loop is O(N), so overall O(N)
# Space Complexity: O(N) - for the monotonic stacks and the prevS / nextS result arrays
def sumSubarrayMins(arr: list[int]) -> int:
    total = 0
    MOD = 10 ** 9 + 7

    def prevSmaller(arr):
        result = [-1] * len(arr)
        stack = []
        for i in range(len(arr)):
            if stack == []:
                result[i] = -1
            elif arr[i] <= stack[-1][0]:
                while (len(stack) > 0 and stack[-1][0] > arr[i]):
                    stack.pop()
                if len(stack) > 0:
                    result[i] = stack[-1][1]
                else:
                    result[i] = -1
            else:
                result[i] = stack[-1][1]
            stack.append([arr[i], i])
        return result

    def nextSmaller(arr):
        n = len(arr)
        result = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            el = arr[i]
            if stack == []:
                result[i] = n
            elif stack[-1][0] < el:
                result[i] = stack[-1][1]
            else:
                while (len(stack) > 0 and stack[-1][0] >= el):
                    stack.pop()
                if len(stack) > 0:
                    result[i] = stack[-1][1]
                else:
                    result[i] = n
            stack.append([arr[i], i])
        return result

    prevS = prevSmaller(arr)
    nextS = nextSmaller(arr)
    for i in range(len(arr)):
        contribution = (i - prevS[i]) * (nextS[i] - i)
        total = (total + contribution * arr[i])

    return total % MOD


print(sumSubarrayMins([11,81,94,43,3]))