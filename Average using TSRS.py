def average(*t): 
    A = sum(t) / len(t)
    return A
print("Average is:",average(10, 20))
print("Average is:",average(10, 20, 30, 50))
print("Average is:",average(10, 20, 40, 50, 80))
print("Average is:",average(10, 20, 30))
