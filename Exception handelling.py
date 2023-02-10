'''
a = 7
b = 0
 Critical situation 
c = a / b

print(c)
'''
a = 7
b = 0
c = 0

try:
    print("File opened")
    b = int(input("Enter a number: "))
    if a == b:
        raise ArithmeticError()
    c = a / b
    print(c)

except ZeroDivisionError:
    print("You can not divide by Zero")
except ValueError:
    input("Enter a number: ")
except ArithmeticError:
    print("Number can't be same")
except Exception:
    print("There might be one issue")
else:
    print(c)
finally:
    print("File Closed")
print("BYE")
