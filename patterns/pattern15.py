# A B C D E 
# A B C D
# A B C 
# A B 
# A 

def printPattern15(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print(f"{chr(65+j)} ", end=" ")
        print()

printPattern15(5)