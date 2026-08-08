#     *
#    ***
#   *****
#  ******* 
#  ******* 
#   *****
#    ***
#     *

def printPattern8(n):
    for i in range(n):
        for j in range(n - i):
            print(" ", end="")
        for k in range(0, ((i + 1)*2) - 1):
            print("*", end="")
        print()
    for i in range(n):
        for j in range(i + 1):
            print(" ", end="")
        for k in range(((n - i)*2) - 1):
            print("*", end="")
        print()

    
printPattern8(4)
