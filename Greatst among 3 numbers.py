input("Enter 3 numbers:")
a, b, c = int(input()), int(input()), int(input())
'''if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c) '''
print((a if a > c else c) if a > b else (b if b > c else c))

