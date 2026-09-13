# Magnetic Force Between Two Balls 
# Input: position = [1,2,3,4,7], m = 3
# Output: 3
# Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
# https://leetcode.com/problems/magnetic-force-between-two-balls/description/ 

# Time Complexity: O(n) — single pass through the positions array
# Space Complexity: O(1) — constant extra space
def canWePlace(arr:list[int], d:int, m:int) -> bool:
    n = len(arr) 
    ball_count = 1 
    last_ball_at = arr[0] 
    for i in range(1, n):
        if arr[i] - last_ball_at >= d:
            ball_count += 1 
            last_ball_at = arr[i] 
            if ball_count == m:
                return True 
    return False


# Time Complexity: O(n log(max_dist)) — binary search over distance range [1, max-min] (log(max_dist) steps),
#                  each step calls canWePlace which is O(n). Sorting is O(n log n),
#                  which is dominated by O(n log(max_dist)) when max_dist is large.
# Space Complexity: O(n) — for the sorted copy of position (Python's sorted() creates a new list)
def maxDistance(position: list[int], m: int) -> int:
    n = len(position) 
    position = sorted(position)
    low = 1 
    high = position[n - 1] - position[0] 
    while low <= high:
        mid = low + (high - low) // 2 
        can_we_place = canWePlace(position, mid, m) 
        if can_we_place == False:
            high = mid - 1 
        else:
            low = mid + 1 
    return high