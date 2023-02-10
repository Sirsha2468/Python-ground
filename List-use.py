l1 = [40, 20, 30]
for x in l1:
    if x == 20:
        del x # Nothing will happen as we are deleting x not l1
print(l1)
l1 = [ [1, 3, 5], [2, 1, 8], [5, 4, 4]]
for row in l1:
    print(row)
for row in l1:
    for e in row:
        print( e , end = '')
    print()
