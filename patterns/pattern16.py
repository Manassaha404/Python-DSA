# A 
# B B 
# C C C 
# D D D D
# E E E E E 

def printPattern16(n):
    for i in range(n):
        for j in range(i + 1):
            print(f"{chr(65 + i)} ", end=" ")
        print()
printPattern16(4)