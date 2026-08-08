# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

def printPattern19(n):
    for i in range(n):
        for j in range(n - i,0,-1):
            print("*", end="")
        for j in range(0, ((i+1) * 2) - 2):
            print(" ", end="")
        for j in range(n - i,0,-1):
            print("*", end="")
        print()
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        for k in range(((n-i)*2)-2, 0, -1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print() 

printPattern19(5)