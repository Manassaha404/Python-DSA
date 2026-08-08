# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3 
# 1 2 
# 1

def printPattern6(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(f"{j} ", end=" ")
        print()

printPattern6(5)