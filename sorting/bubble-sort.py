
# Bubble Sort Theory:
# - Concept: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The largest elements "bubble" up to the end.
# - Time Complexity: O(n) Best case (already sorted), O(n^2) Average/Worst cases.
# - Space Complexity: O(1) (In-place sorting).


def swap(array:list[int], index1:int, index2:int ):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def bubbleSort(list:list[int]):
    n = len(list)
    for i in range(n-1, 0, -1):
        isSorted = True
        for j in range(i):
            if list[j] > list[j+1]:
                isSorted = False
                swap(list, j, j+1)
        if isSorted:
            break

a = [7,5,2,3,32,3] 
b = [2, 3, 3, 5, 7, 32] 
bubbleSort(b)
print(b)

