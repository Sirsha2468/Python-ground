'''Last digit from a three digit number'''
n = int(input("Enter a 3 digit number: "))
if n >= 100 and n <= 999:
    n1 = n % 10 # n1 = 125 % 10 = 5
    print(int(n1))
else:
    print("Please enter a 3 digit number, and try again")
    
