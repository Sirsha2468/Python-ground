#Armstrong number using recursive approach
number = int(input("Enter a number: "))
#Taking input from user
order = len(str(number))
sum = 0
#Assigning the value of sum = 0
temp = number

#going through every digit of number store in temp variable
while temp > 0:
    n = temp % 10
    temp = temp // 10
#Storing the sum of cube of the digits in sum variable
    sum = sum + pow(n, order)
if(sum == number):
    print(number," is an armstrong number")
else:
    print(number," is not an armstrong number")
