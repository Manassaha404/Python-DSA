# Time Complexity  : O(n) — worst case scans every element once (target at end or absent)
# Space Complexity : O(1) — no extra data structures, only the loop index `i`
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

a = [3,43,2,42,4,24234,23,424,4,24,4236,463,4345,34,54]
ans = linear_search(a, 4) 
print(ans)
