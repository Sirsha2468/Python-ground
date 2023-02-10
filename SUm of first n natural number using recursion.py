def f1(n):
    n = int(input("Enter the number: "))
    if n == 1:
        s = n + f1(n-1)
        print(s)
        return s;
f1(4)

