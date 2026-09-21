# search a element in a array using recursion 
# [1,3,2,8,45,32,98,23,2,3,4] target = 8 
# ans -> 3 
def linearSearch(arr:list[int], target:int, cur = 0):
    if cur == len(arr):
        return -1 
    if arr[cur] == target:
        return cur 
    else:
        return linearSearch(arr, target, cur + 1) 


print(linearSearch([1,3,2,8,45,32,98,23,2,3,4], 8)) 


def linearSearchAllIndex(arr:list[int], target:int):
    result = [] 
    def helper(arr:list[int], target:int, cur = 0):
        nonlocal result
        if cur == len(arr):
            return
        if arr[cur] == target:
            result.append(cur) 
        helper(arr, target, cur + 1)
    helper(arr, target) 
    return result 


print(linearSearchAllIndex([1,3,2,8,45,32,98,23,2,3,4], 2))


        

