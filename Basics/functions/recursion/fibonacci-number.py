def sumOfFibonacciNumber(n:int):
    if (n <= 1):
        return n
    return sumOfFibonacciNumber(n - 1) + sumOfFibonacciNumber(n - 2)

print(sumOfFibonacciNumber(5))

# Time Complexity -> O(2ⁿ) — exponential.
# Space complexity -> O(n) 



