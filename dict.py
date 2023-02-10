d1 = {102: 'Sirsha', 105: 'payal'}
print(d1)
print(d1[102]) #We can access it by the key value here 102 is the key value
for k in d1:
    print(k)
    print(k, d1[k])
d1[102] = 'Ravi' # Here Ravi is replaced in the place of Sirsha
print(d1)
d1[105] = ('Rahul', 'Dilip') # We can't change the value of keys but we can rechange the element value inside.
print(d1)
del d1[102] #By this process we can delete any element from the dict
print("After deletion our dictionary is: ", d1)
d1[102] = 'Ravi' #By this thng we can edit or add key elements
print(d1)
print(d1.items()) # Returns collection of elements
print(type(d1.items())) # Dict item classes object
for t in d1.items():
    print(t,"\n")
for k,v in d1.items():
    print(k, v)
#print(dict_values([105, 102]))
for v in d1.values():
    print(v)
print("Length of d1 is:",len(d1))
print("Minimum of d1 is:", min(d1))
print("Maximum of d1 is:", max(d1))
print("Sorted list of key is: ", sorted(d1))
print("Popped element is:",d1.pop(102))
print(d1)
d1[102] = "Ravi"
print(d1)
print(d1.popitem()) #Here we can delete item and list
#Wap to enter from user
