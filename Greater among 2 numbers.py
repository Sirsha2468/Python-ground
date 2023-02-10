'''a = int(input("Enter the number: "))
b =int(input("Enter the number: "))
if a > b:
    print(a)
else:
    print(b)
'''
# Smarter and precise code
print("Enter 2 numbers: ")
a, b = int(input()), int(input())
print(a if a > b else b)
