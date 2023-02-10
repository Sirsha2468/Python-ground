x = eval(input("Enter a number: "))
#We can enter variety of data type using eval()
match x:
    case 1:
        print("One", type(x))
    case "2":
        print("Two", type(x))
    case 2:
            print("Two", type(x))
    case 3:
        print("Three", type(x))
    case True:
        print("Four", type(x))
