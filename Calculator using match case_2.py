x = int(input())
eval = ("Enter the value of X, Y, Z: ")
X = input()
Y = input()
Z = input()
match x:
    case 1:
        if(X == Y or X == Z or Y == Z):
            print("This is Isoscelas triangle")
        else:
            print("Not")
    case 2:
        if(X**2 + Y**2 == Z**2 or Y**2 == X**2 + Z**2 or X**2 == Z**2 + Y**2):
            print("This is a right angle triangle")
        else:
            print("NOT")
    case 3:
            if(X == Y and X == Z and Y == Z):
                print("This is Isoscelas triangle")
            else:
                print("Not an isoscelas triangele")

        
