x = int(input("1 - addition, 2 - substraction, 3 - multiplicarion, 4 - divition"))
match x:
    case 1:
        a = eval(input("Enter 1st number: "))
        b = eval(input("Enter 2nd number: "))
        print(a + b)
    case 2:
        a = eval(input("Enter 1st number: "))
        b = eval(input("Enter 2nd number: "))
        print(c = a - b)
    case 3:
        a = eval(input("Enter 1st number: "))
        b = eval(input("Enter 2nd number: "))
        print(c = a * b)
    case 4:
        a = eval(input("Enter 1st number: "))
        b = eval(input("Enter 2nd number: "))
        print(c = a / b)
    case _:
        print("Enter correct choice: ")
        
    
