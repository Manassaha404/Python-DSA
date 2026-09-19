# find n'th fibonacci number 
# fibonacci number -> 0 1 1 2 3 5 8 13 . . . 

def nthFibo(n:int) -> int:
    if n <= 1:
        return n 

    return nthFibo(n - 1) + nthFibo(n - 2) 

# Time Complexity: O(2^n) - each call branches into 2 more calls (exponential growth)
# Space Complexity: O(n)  - maximum call stack depth is n (height of recursion tree)

print(nthFibo(6))


