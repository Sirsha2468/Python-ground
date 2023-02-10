number = int(input("Enter a number: "))
order = len(str(number))
sum = 0
temp = number

while temp > 0:
    n = temp % 10
    sum = n ** order
    temp = temp // 10
if number == sum:
    print(number, "is an armstrong number")
else:
    print(number, "is not an armstrong number")
