# Median of Two Sorted Arrays 
# arr1 = [1,2,5,8,12]
# arr2 = [2,4,6,10,13]
# ans = 5.5 
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/ 
# brute force approach: merge the two arrays and find the median.
# Time Complexity  : O(n1 + n2) — single pass to merge both arrays
# Space Complexity : O(n1 + n2) — extra space for the merged array
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    index1 = n // 2 - 1
    index2 = n // 2
    merged = [] 
    left = 0
    right = 0
    while left < n1 and right < n2:
        if nums1[left] < nums2[right]:
            merged.append(nums1[left])
            left += 1 
        else:
            merged.append(nums2[right])
            right += 1
    while left < n1:
        merged.append(nums1[left])
        left += 1
    while right < n2:
        merged.append(nums2[right])
        right += 1
    if n % 2 == 0:
        return (merged[index1] + merged[index2]) / 2
    else:
        return merged[index2]   


# better approach: reduce the space complexity to O(1) by using two pointers to find the median without merging the arrays.
# Time Complexity  : O(n1 + n2) — single pass through both arrays using two pointers
# Space Complexity : O(1) — no extra space used, only two median variables tracked
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    index1 = n // 2 - 1
    index2 = n // 2
    left = 0
    right = 0
    count = -1
    median1 = 0
    median2 = 0
    while left < n1 and right < n2:
        el = None 
        if nums1[left] < nums2[right]:
            el = nums1[left]
            left += 1 
        else:
            el = nums2[right]
            right += 1
        count += 1
        if count == index1:
            median1 = el
        if count == index2:
            median2 = el
            break
    while left < n1:
        el = nums1[left]
        left += 1
        count += 1
        if count == index1:
            median1 = el
        if count == index2:
            median2 = el
            break
    while right < n2:
        el = nums2[right]
        right += 1
        count += 1
        if count == index1:
            median1 = el
        if count == index2:
            median2 = el
            break
    if n % 2 == 0:
        return (median1 + median2) / 2
    else:
        return median2



# optimal approach: binary search on the smaller array to find the correct partition point
#  that divides the two arrays into two halves such that all elements in the left half are less than or equal
#  to all elements in the right half. The median can then be calculated based on the maximum
#  of the left half and the minimum of the right half.
# Time Complexity  : O(log(min(n1, n2))) — binary search is performed only on the smaller array
# Space Complexity : O(1) — only a constant number of variables are used
def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    n1 = len(nums1) 
    n2 = len(nums2)  
    if n2 < n1:
        return self.findMedianSortedArrays(nums2, nums1)
    n = n1 + n2
    low = 0 
    high = n1 
    left = (n + 1) // 2 
    while low <= high:
        mid1 = low + (high - low) // 2 
        mid2 = left - mid1 
        l1 = float("-inf")
        l2 = float("-inf")
        r1 = float("inf")
        r2 = float("inf") 
        if mid1 < n1:
            r1 = nums1[mid1] 
        if mid2 < n2:
            r2 = nums2[mid2] 
        if mid1 - 1 >= 0 and mid1 - 1 < n1:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0 and mid2 - 1 < n2:
            l2 = nums2[mid2 - 1] 
        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2) 
            else:
                return (max(l1, l2) + min(r1,r2)) / 2 
        elif l1 > r2:
            high = mid1 - 1 
        elif l2 > r1:
            low = mid1 + 1 
    return 0



# kth element of two sorted arrays: 
# nums1 = [1, 3, 5, 7, 9]
# nums2 = [2, 4, 6, 8, 10]
# k = 5
# ans = 5
# Time Complexity  : O(log(min(n1, n2))) — binary search is performed only on the smaller array
# Space Complexity : O(1) — only a constant number of variables are used
def kthElementOfTwoSortedArrays(self, nums1: list[int], nums2: list[int], k: int) -> int:
    n1 = len(nums1) 
    n2 = len(nums2)  
    if n2 < n1:
        return self.findMedianSortedArrays(nums2, nums1)
    n = n1 + n2
    low = max(0, k - n2)
    high = min(k, n1)
    left = k
    while low <= high:
        mid1 = low + (high - low) // 2 
        mid2 = left - mid1 
        l1 = float("-inf")
        l2 = float("-inf")
        r1 = float("inf")
        r2 = float("inf") 
        if mid1 < n1:
            r1 = nums1[mid1] 
        if mid2 < n2:
            r2 = nums2[mid2] 
        if mid1 - 1 >= 0 and mid1 - 1 < n1:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0 and mid2 - 1 < n2:
            l2 = nums2[mid2 - 1] 
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)  
        elif l1 > r2:
            high = mid1 - 1 
        elif l2 > r1:
            low = mid1 + 1 
    return 0

