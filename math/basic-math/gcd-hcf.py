# gcd -> greatest common factor 
# hcf -> highest common factor 

# 24 -> [1, 2, 13, 26] 
# 34 -> [1, 2, 17, 34] 

# gcd is 2 

# brute force 
def findGcdByBruteForce(a:int, b:int):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

print(findGcdByBruteForce(24,34)) # gcd -> 2 
# Time complexity: O(min(a, b))


# euclidean algo
# gcd(a,b) -> gcd(a - b, b) {a > b}

# so, gcd(34,24) -> gcd(10,34) -> gcd(34,10) -> gcd(24,10) -> gcd(14,10) -> gcd(4,10) ->
# gcd(10,4) -> gcd(6,4) -> gcd(2,4) -> gcd(4,2) -> gcd(2,2) -> gcd(0,2)  -> gcd is 2 

# but still lot of steps 
# better approach 
# gcd(a,b) -> gcd(a % b) {a > b}

# so, 
# gcd(34,24) -> gcd(10,24) -> gcd(24,10) -> gcd(4, 10) -> gcd(10,4) -> gcd(2,4) -> 
# gcd(4,2) -> gcd(0,2) -> gcd is 2 

def findGcd(a:int, b:int):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a

    return b if a == 0 else a 

print(findGcd(24,34))

# Time complexity: O(log(min(a, b)))


