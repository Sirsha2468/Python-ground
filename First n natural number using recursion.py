def printN(n):
    if n > 0:
        printN(n-1)
        print(n)
printN(6)
