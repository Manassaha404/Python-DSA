# intersection of two sorted array 
# nums1 = [1,2,3,3,5,7,8,9,10] 
# nums2 = [1,4,5,6,9]
# intersection_array = [1,5,9]


def getIntersection(nums1:list[int], nums2:list[int]):
    i = 0
    j = 0
    intersection_array = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersection_array.append(nums1[i])
            i += 1
            j += 1
            continue
        if nums1[i] > nums2[j]:
            j += 1
            continue
        i += 1
    return intersection_array

# Time Complexity: O(M + N) - single two-pointer pass; M and N are the lengths of nums1 and nums2
# Space Complexity: O(min(M, N)) - output array holds at most min(M, N) elements; O(1) auxiliary space

nums1 = [1,2,3,3,5,6,6,7,8,9,10]
nums2 = [1,3,4,5,6,9] 
intersection = getIntersection(nums1, nums2)
print(intersection)

        


