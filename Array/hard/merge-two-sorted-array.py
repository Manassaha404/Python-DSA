# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 
# -> [1,2,2,3,5,6] 
# https://leetcode.com/problems/merge-sorted-array/description/ 

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None: 
    # Time Complexity: O(M + N), where M and N are the given lengths, as we iterate through both arrays once.
    # Space Complexity: O(1), as the merging is done in-place within nums1.
    j = m + n - 1
    i = m - 1
    k = n - 1
    while k >= 0: 
        if i >= 0 and nums2[k] < nums1[i]:
            nums1[j] = nums1[i] 
            i -= 1
        else:
            nums1[j] = nums2[k]
            k -= 1 
        j -= 1 