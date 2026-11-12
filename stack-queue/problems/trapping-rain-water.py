# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/

def trap(height: list[int]) -> int:
    # Approach 1: Prefix and Suffix Max arrays (commented out)
    # Time Complexity  : O(N) — 3 passes over the array (prefixMax, suffixMax, water calculation)
    # Space Complexity : O(N) — auxiliary prefixMax and suffixMax arrays of size N
    # n = len(height)
    # total = 0
    # suffixMax = [0] * n
    # preffixMax = [0] * n
    # suffixMax[n - 1] = height[n - 1]
    # preffixMax[0] = height[0]
    # for i in range(n - 2, -1, -1):
    #     suffixMax[i] = max(suffixMax[i + 1], height[i])
    # for i in range(1, n):
    #     preffixMax[i] = max(preffixMax[i - 1], height[i])
    # for i in range(n):
    #     leftMax = preffixMax[i]
    #     rightMax = suffixMax[i]
    #     if leftMax > height[i] < rightMax:
    #         total += (min(leftMax, rightMax) - height[i])
    # return total

    # Approach 2: Suffix Max array + running Left Max variable (commented out)
    # Time Complexity  : O(N) — 2 passes over the array (suffixMax and running leftMax)
    # Space Complexity : O(N) — auxiliary suffixMax array of size N
    # n = len(height)
    # total = 0
    # leftMax = 0
    # suffixMax = [0] * n
    # suffixMax[n - 1] = height[n - 1]
    # for i in range(n - 2, -1, -1):
    #     suffixMax[i] = max(suffixMax[i + 1], height[i])
    # for i in range(n):
    #     leftMax = max(leftMax, height[i])
    #     rightMax = suffixMax[i]
    #     if leftMax > height[i] < rightMax:
    #         total += (min(leftMax, rightMax) - height[i])
    # return total

    # Approach 3: Two Pointers (active)
    # Time Complexity  : O(N) — single pass where two pointers meet in N steps
    # Space Complexity : O(1) — constant extra space using pointers and running max variables
    n = len(height)
    h = height
    l, r = 0, n -1
    leftMax, rightMax  = 0, 0
    total = 0
    while l < r:
        if h[l] <= h[r]:
            leftMax = max(leftMax, h[l])
            total += leftMax - h[l]
            l += 1
        else:
            rightMax = max(rightMax, h[r])
            total += rightMax - h[r]
            r -= 1
    return total