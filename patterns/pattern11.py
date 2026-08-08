# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1
# 1 0 1 0 1

def changeCurrent(n):
    if n == 1:
        return 0
    else:
        return 1

def printPattern11(n):
    current = 1;
    for i in range(n):
        for j in range(i + 1):
            print(f"{current} ", end="")
            current = changeCurrent(current);
        print()

printPattern11(4)


