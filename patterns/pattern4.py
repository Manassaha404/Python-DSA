# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 

def printPattern4(n):
    for i in range(n):
        for j in range(i + 1):
            print(f"{i + 1} ", end=" ")
        print()
printPattern4(4)