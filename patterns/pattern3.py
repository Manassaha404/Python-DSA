# 1 
# 1 2
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

def printPattern3(n):
    for i in range(n):
        for j in range(i + 1):
            print(f"{j + 1} ", end=" ")
        print()

printPattern3(5)