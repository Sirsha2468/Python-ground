i = 1
while i <= 3:
    a = int(input("Enter an even number: "))
    if a%2 == 0:
        print("You win the game")
        break #Terminates the loop 
    i+=1
else:
    print("Game over")


    
