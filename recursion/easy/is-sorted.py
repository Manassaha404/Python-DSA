# check if the array is sorted or not using recursion 
def isSorted(arr:list[int], cur = 0):
    if cur == len(arr) - 1:
        return True 
    if arr[cur] <= arr[cur + 1]:
        return isSorted(arr, cur + 1) 
    else:
        return False 

print(isSorted([1,2,3,4,5,6,4]))


