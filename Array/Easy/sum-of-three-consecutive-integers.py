# three consecutive integers that sum to given number 
# 33 -> [10,11,12] 
# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/description/


def sumOfThree( num: int) -> list[int]:
    result = [] 
    if num % 3 == 0:
        q = num // 3 
        result = [q - 1, q,q + 1]
    return result


print(sumOfThree(4))
    

        