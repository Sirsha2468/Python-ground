def fib(n):
    a, b = 0, 1
    while n:
        yield a
        a, b = b, a+b
        n-=1
for e in fib(int(input("Enter a number: "))):
    print(e, end = ' ')
