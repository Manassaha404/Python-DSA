"""

 MERGE SORT — Theory


CONCEPT:
  Merge Sort is a classic Divide-and-Conquer algorithm.
  It works in two major phases:
    1. DIVIDE  : Recursively split the array into two halves
                 until each sub-array contains a single element
                 (a single element is always sorted).
    2. MERGE   : Repeatedly merge the sorted sub-arrays back
                 together in the correct order.

HOW IT WORKS (step-by-step):
  Given: [7, 5, 2, 3]
    Divide  →  [7, 5]  |  [2, 3]
    Divide  →  [7] [5] |  [2] [3]
    Merge   →  [5, 7]  |  [2, 3]
    Merge   →  [2, 3, 5, 7]

MERGE STEP:
  - Use two pointers (left, right) to compare elements from
    both halves and build a sorted temporary array.
  - Copy remaining elements from whichever half isn't exhausted.
  - Write the temp array back into the original array.

COMPLEXITY:
  ┌────────────┬──────────────┐
  │ Case       │ Time         │
  ├────────────┼──────────────┤
  │ Best       │ O(n log n)   │
  │ Average    │ O(n log n)   │
  │ Worst      │ O(n log n)   │
  ├────────────┼──────────────┤
  │ Space      │ O(n)         │
  └────────────┴──────────────┘
  - log n  → depth of recursion tree (halving each time)
  - n      → work done at each level (merging all elements)
  - Space is O(n) due to the temporary array used in merge.

KEY PROPERTIES:
  ✔ Stable Sort    : Preserves relative order of equal elements.
  ✔ Not In-place   : Requires O(n) extra memory.
  ✔ Consistent     : Always O(n log n) regardless of input.
  ✔ Preferred for  : Linked lists, external sorting (large data).

"""

def merge(arr:list[int], low:int, mid:int, high:int):
    temp:list[int] = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]



def mergeSort(arr:list[int], low:int, high:int):
    if low >= high:
        return

    mid = low + (high - low) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)

def sort(arr:list[int]):
    low = 0
    high = len(arr) - 1
    mergeSort(arr, low, high)

a = [7,5,2,3,32,3] 
sort(a)
print(a)

