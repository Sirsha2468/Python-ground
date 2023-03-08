# # Program to generate a random number between 0 and 100
# import random

# print(random.randint(0, 100));

# Swap using xor logic
# a = eval(input("Enter the first integer: "))
# b = eval(input("Enter the 2nd integer: "))

# a = a ^ b; # a = 10, b = 20 || a = 10 ^ 20 = 30
# b = a ^ b; # b = 30 ^ 20 = 10
# a = a ^ b; # a = 30 ^ 10 = 20 
# # Now a = 20, b = 10

# print("The value of a is",a,"and b is",b)

# Program to interchange km to mile

# km = eval(input("Enter the length in KM: "));
# print(km,"km is", km / 1.609, "mile");

# Program to convert Celcius to Farenhite 
# celcius = eval(input("Enter the temarature in Celcius: "));
# print(celcius, "degree celcious in Farenhite is", (celcius * 1.8) + 32,"degree");
# Progra, to check whether a number is positive, non positive and negetive.....
# num = eval(input("Enter a number: "))

# if (num == 0):
#     print(num, "is non positive/negetive");
# elif (num > 0):
#         print(num,"is a positive number");
# else:
#         print(num, "is a negetive number");
WAP to check whether a number is odd or even
# n = eval(input("Enter a integer: "))
# WAP to check leap year

Year = eval(input("Enter a year for checking leap year: "));

if (Year % 400 == 0) and (Year % 100 == 0):
    print("{0} is a leap year".format(Year))
    
# Not divided by 100 means not a century year
# Year divided by 4 is a leap year
elif (Year % 4 == 0) and (Year % 100 != 0):
    print("{0} is a leap year".format(Year))
    
# if not divided by both 400 (century year) and 4 (not a century year)
# Year is not leap year
else:
    print("{0} is not a leap year" .format(Year))
    
# if(n % 2 == 0):
#     print(n, "is even")
# else:
#     print(n, "is odd")
