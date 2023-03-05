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
num = eval(input("Enter a number: "))

if (num == 0):
    print(num, "is non positive/negetive");
elif (num > 0):
        print(num,"is a positive number");
else:
        print(num, "is a negetive number");
