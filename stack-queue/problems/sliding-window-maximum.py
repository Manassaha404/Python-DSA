# Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    # Approach 1: Monotonic Deque with window bounds check before append (commented out)
    # Time Complexity  : O(N) — each index is pushed and popped from the deque at most once
    # Space Complexity : O(k) — deque stores at most k indices (plus O(N - k + 1) for result list)
    # queue = deque()
    # l = 0
    # result = []
    # for i in range(len(nums)):
    #     while queue and nums[queue[-1]] <= nums[i]:
    #         queue.pop()
    #     while queue and i - queue[0] + 1 > k:
    #         queue.popleft()
    #     queue.append(i)
    #     if i - l + 1 == k:
    #         result.append(nums[queue[0]])
    #         l += 1
    # return result

    # Approach 2: Monotonic Deque with left pointer boundary check (active)
    # Time Complexity  : O(N) — each index is pushed and popped from the deque at most once
    # Space Complexity : O(k) — deque stores at most k indices of the window (plus O(N - k + 1) for result list)
    queue = deque()
    l = 0
    result = []
    for i in range(len(nums)):
        while queue and nums[queue[-1]] <= nums[i]:
            queue.pop()
        queue.append(i)
        if l > queue[0]:
            queue.popleft()
        if i + 1 >= k:
            result.append(nums[queue[0]])
            l += 1
    return result

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


