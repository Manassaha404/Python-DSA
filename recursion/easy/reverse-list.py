def swap(index1:int, index2:int, array:list[int]):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp
# Time Complexity: O(1) - constant time swap
# Space Complexity: O(1) - no extra space used


def reverseList(list:list[int], i = 0):
    if i >= len(list)//2:
        return

    swap(i, len(list) - 1 - i, list)
    reverseList(list,i + 1)
# Time Complexity: O(n) - n/2 recursive calls are made (one per pair)
# Space Complexity: O(n) - O(n/2) ≈ O(n) call stack frames


a = [7,5,2,3,32,3]
reverseList(a)
print(a)


