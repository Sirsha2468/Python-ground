n = int(input("Enter a 3 digit number: "))
if n >= 100 and n <= 999:
    n1 = n / 10 # n1 = 125 / 10 = 12
    n2 = n1 % 10 # 12 % 10 = 2
    print(int(n2))
else:
    print("Please enter a 3 digit number, and try again")
    
