#     *
#    ***
#   *****
#  ******* 

def printPattern7(n):
    for i in range(n):
        for j in range(n - i):
            print(" ", end="")
        for k in range(((i + 1)*2) - 1):
            print("*", end="")
        print()
printPattern7(4)

