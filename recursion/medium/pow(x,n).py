# Pow(x, n)
# https://leetcode.com/problems/powx-n/description/ 
def myPow(x: float, n: int) -> float:
    ans = 1.0
    m = n
    n = abs(n)
    def helper(x, n):
        nonlocal ans
        if n == 0:
            return
        if n % 2 == 0:
            n = n // 2
            x = x * x
            helper(x, n)
        else:
            n = n - 1
            ans = ans * x
            helper(x, n)
    helper(x, n)
    if m < 0:
        return 1 / ans
    return ans

# Time Complexity: O(log n) - binary exponentiation divides n by 2 at each even step (at most 2 * log2(n) recursive calls)
# Space Complexity: O(log n) - recursion call stack depth is proportional to log2(n)

print(myPow(2.00000, -2))

