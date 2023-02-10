s1 = {1, 5, 8}
s2 = {10, 2, 8, 10, 10, 8}
s3 = {} # This is not a set. This is dict.
#Ss4 = set(10)
print(type(s3))
print(s3)
#We have to use set function to make an empty set object
s3 = set()
print(type(s1))
print(s1)
print(s2) #  {8, 10, 2} will come as duplicate values are not allowed in set.
print(type(s3))
#print("This is s4", s4) //TypeError: 'int object is not iterable

print(len(s1))
print(sum(s2))
print(sorted(s2))
print(s1.add(12))
s1.update([10, 20], 'ABC', range(20,24,1))
print(s1)
s1.remove([1, 5])
print(s1.remove([1, 5]))
