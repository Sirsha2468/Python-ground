s1 = input("What is your favourite color? ")
l1 = ["yellow", "blue", "orange", "white", "black", "red"]
for colour in l1:
    if  colour in l1:
        if colour in s1:
            c = colour
            break
    else:
        c = "other"
    match c:
        case "yellow":
            print("Monday")
        case "blue":
            print("Tuesday")
        case "orange":
            print("Wednesday")
        case "white":
            print("Thursday")
        case "black":
            print("Friday")
        case "red":
            print("Saturday")
        
