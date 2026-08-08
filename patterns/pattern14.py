# A 
# A B 
# A B C 
# A B C D 

def printPattern14(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print()
printPattern14(4)
