# 5 5 5 5 5 5 5 5 5 
# 5 4 4 4 4 4 4 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 2 1 2 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 4 4 4 4 4 4 5 
# 5 5 5 5 5 5 5 5 5


# first convert to this ---> 
# 0 0 0 0 0 0 0 0 0
# 0 1 1 1 1 1 1 1 0
# 0 1 2 2 2 2 2 1 0
# 0 1 2 3 3 3 2 1 0
# 0 1 2 3 4 3 2 1 0
# 0 1 2 3 3 3 2 1 0
# 0 1 2 2 2 2 2 1 0
# 0 1 1 1 1 1 1 1 0
# 0 0 0 0 0 0 0 0 0



def printPattern22(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j 
            bottom = 2*n - 2 - i 
            right = 2*n - 2 - j
            val = n - min(min(top,bottom),min(left, right))
            print(val, end=" ")
        print()

printPattern22(5)


