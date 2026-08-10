def swap(index1:int, index2:int, array:list[int]):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def reverseList(list:list[int], i = 0):
    if i >= len(list)//2:
        return

    swap(i, len(list) - 1 - i, list)
    reverseList(list,i + 1)


a = [7,5,2,3,32,3]
reverseList(a)
print(a)

# Time complexity: O(n)
# Space complexity: O(n)


