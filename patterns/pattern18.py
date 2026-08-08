# E 
# D E 
# C D E 
# B C D E 
# A B C D E 


def printPattern18(n):
    for i in range(n,0,-1):
        for j in range(i,n + 1):
            print(f"{chr(65 + j -1)} ", end="")
        print()

        
printPattern18(5)