month = int(input("Enter the number of month: "))
match month:
    case 1:
        if month in (1, 3, 5, 7, 8, 10, 12):
            print("31 Days")          
    case 2:
        if month in (4, 6, 9, 11):
            print("30 Days")
    case 3:
        if month == 2:
            print("28 or 29 days")
    case 4:
        print("Invalid month number")          
