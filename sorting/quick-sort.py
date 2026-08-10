# Quick Sort Theory
# 
# Okay so imagine you have a messy pile of cards on the table.
# Instead of comparing every card with every other card,
# you pick ONE card — call it the "pivot" — and then say:
#
#   "Everything smaller than this goes LEFT,
#    everything bigger goes RIGHT."
#
# Now you've got two smaller piles. You do the SAME thing
# to each pile recursively... and boom, the whole thing
# gets sorted without much effort per step.
#
# That's literally Quick Sort. Divide and Conquer.
#
# ------------------------------------------------------------
#  HOW IT WORKS (step by step):
# ------------------------------------------------------------
#
#  1. Pick a PIVOT element (here we pick the first element).
#
#  2. PARTITION the array:
#       - Use two pointers: i from the left, j from the right.
#       - Move i forward until you find something BIGGER than pivot.
#       - Move j backward until you find something SMALLER/EQUAL.
#       - If i < j, swap arr[i] and arr[j].
#       - Keep doing this until i and j cross each other.
#       - Finally, swap the pivot (arr[low]) with arr[j].
#       - Now pivot is at its CORRECT final position!
#
#  3. Recursively sort:
#       - Left part  → arr[low ... partition-1]
#       - Right part → arr[partition+1 ... high]
#
# ------------------------------------------------------------
#  WHY IT'S FAST:
# ------------------------------------------------------------
#
#  Average Case: O(n log n)    — pivot splits array roughly in half each time
#  Worst Case:  O(n²)          — happens when pivot is always smallest/largest
#                                (e.g., already sorted array + picking first as pivot)
#  Space:       O(log n)       — recursive call stack (no extra array like Merge Sort)
#




def swap(array: list[int], index1: int, index2: int):
    # Classic swap — just swap two elements using a temp variable
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def partitionFuc(arr: list[int], low: int, high: int):
    # We pick the FIRST element as our pivot
    pivot = arr[low]

    i = low   # i moves right, looking for something > pivot
    j = high  # j moves left, looking for something <= pivot

    while i <= j:
        # Keep moving i right while elements are <= pivot
        while i <= high and arr[i] <= pivot:
            i += 1
        # Keep moving j left while elements are > pivot
        while j >= low and arr[j] > pivot:
            j -= 1
        # If pointers haven't crossed, swap the out-of-place elements
        if i < j:
            swap(arr, i, j)

    # Put the pivot in its correct sorted position
    swap(arr, low, j)

    # Return pivot's final index — the partition point
    return j


def quickSort(arr: list[int], low: int, high: int):
    # Base case: if the subarray has 1 or 0 elements, it's already sorted
    if low >= high:
        return

    # Find the pivot's correct position after partitioning
    partition = partitionFuc(arr, low, high)

    # Recursively sort the left and right halves
    quickSort(arr, low, partition - 1)
    quickSort(arr, partition + 1, high)


def sort(arr: list[int]):
    # Entry point — just set low=0 and high=last index, then let recursion do its thing
    low = 0
    high = len(arr) - 1
    quickSort(arr, low, high)


# --- Test ---
a = [7, 5, 5, 2, 3, 32, 3]
sort(a)
print(a)  # Output: [2, 3, 3, 5, 5, 7, 32]
