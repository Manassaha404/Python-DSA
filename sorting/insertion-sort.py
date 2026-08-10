
# Insertion Sort Theory:
# - Concept: Builds the sorted array one element at a time by repeatedly taking the next unsorted element and inserting it into its correct position in the sorted part.
# - Time Complexity: O(n) Best case (already sorted), O(n^2) Average/Worst cases.
# - Space Complexity: O(1) (In-place sorting).


def swap(array:list[int], index1:int, index2:int ):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def insertionSort(list:list[int]):
    n = len(list)
    for i in range(n-1):
        for j in range(i+1, 0, -1):
            if list[j] < list[j-1]:
                swap(list,j,j-1)
            else:
                break

a = [7,5,2,3,32,3] 
insertionSort(a)
print(a)