# merge intervals 
# [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]] 
# https://leetcode.com/problems/merge-intervals/description/ 

def merge(intervals: list[list[int]]) -> list[list[int]]:
    # Time Complexity: O(N log N), where N is the length of intervals due to the sorting step.
    # Space Complexity: O(N) for the output list `ans` and the space required by Python's TimSort.
    intervals.sort() 
    ans:list[list[int]] = []
    n = len(intervals) 
    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1] 
        ans_last_el_index = len(ans) - 1 
        if ans_last_el_index == -1:
            ans.append([start, end])
            continue 
        if ans[ans_last_el_index][1] >= start and end > ans[ans_last_el_index][1]: 
            ans[ans_last_el_index][1] = end 
        elif ans[ans_last_el_index][1] < start: 
            ans.append([start,end])
    return ans 