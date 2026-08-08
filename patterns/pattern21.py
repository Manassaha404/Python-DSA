# *****
# *   *
# *   *
# *   *
# *****

def printPattern21(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            for j in range(0,n):
                print("*", end="")
        else:
            print("*", end="")
            for j in range(n-2):
                print(" ", end="")
            print("*", end="")
        print()

printPattern21(10)

