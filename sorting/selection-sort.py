
# Selection Sort Theory:
# - Concept: Repeatedly finds the minimum element from the unsorted part and puts it at the beginning.
# - Time Complexity: O(n^2) for Best, Average, and Worst cases.
# - Space Complexity: O(1) (In-place sorting).

def findMinimum(list:list[int], start:int, end:int):
    minimum = start
    for i in range(start, end + 1):
        if list[i] < list[minimum]:
            minimum = i
    return minimum

def swap(array:list[int], index1:int, index2:int ):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def selectionSort(list:list[int]):
    n = len(list)
    for i in range(n-1):
        minimum = findMinimum(list,i,n-1)
        swap(list, i, minimum)

a = [7,5,2,3,32,3] 
selectionSort(a)
print(a)