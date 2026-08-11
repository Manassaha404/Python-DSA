# 1,2,3,3,4,5,6
# 1,4,4,5,8,9
# last = 1 

# Time Complexity  : O(n + m) — each element of nums1 (size n) and nums2 (size m) visited once
# Space Complexity : O(n + m) — output `union` list can hold at most n + m unique elements
def unionTwoSortedArray(nums1:list[int], nums2:list[int]):
    union = []
    n = len(nums1)
    m = len(nums2)
    i = 0
    j = 0
    last_entered = None
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if last_entered != nums1[i]:
                union.append(nums1[i])
                last_entered = nums1[i]
            i += 1
            continue
        if nums1[i] > nums2[j]:
            if last_entered != nums2[j]:
                union.append(nums2[j])
                last_entered = nums2[j]
            j += 1
    while i < n:
        if nums1[i] != last_entered:
            union.append(nums1[i])
            last_entered = nums1[i]
        i += 1
    while j < m:
        if nums2[j] != last_entered:
            union.append(nums2[j])
            last_entered = nums2[j]
        j += 1
    return union

a = [1,2,3,3,4,5,6,9,10,34,67]
b = [1,4,4,5,8,9]

print(unionTwoSortedArray(a,b))
        
