# all divisor of a number 
# 36 -> 1,2,3,4,6,9,12,18,36
import math
def allDivisor(x:int):
    divisor = []
    sqrt = int(math.sqrt(x))
    for i in range(1,sqrt+1):
        if x % i == 0:
            divisor.append(i)
            if x // i != i:
                divisor.append(x//i)
    return sorted(divisor)
print(allDivisor(36))

# time complexity -> O(√x) 