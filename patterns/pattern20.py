# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


def printPattern20(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        for k in range(((n-i)*2)-2, 0, -1):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*", end="")
        for j in range(0, ((n-i+1) * 2) - 2):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()
    

printPattern20(7)
