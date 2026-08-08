# 1      1
# 12    21
# 123  321
# 12344321

def printPattern12(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for k in range((n - i)*2, 0, -1):
            print(" ", end="")
        for j in range(i,0,-1):
            print(j, end="")  
        print()


printPattern12(9)