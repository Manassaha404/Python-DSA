# prime number -> A prime number is a natural number greater than 1 that has exactly two positive divisors: 1 and itself
import math
def isPrime(x:int):
    count = 0
    sqrt = int(math.sqrt(x))
    for i in range(1,sqrt+1):
        if x % i == 0:
            count += 1
            if x // i != i:
                count += 1
    return True if count == 2 else False

print(isPrime(13))
