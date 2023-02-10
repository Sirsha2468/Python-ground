#s = input("Enter a string: ")
s = input("Enter elements separated by comma: ")
#s1 = {e for e in s if e in "aeiou"}
s1 = {e for e in s.split(',')}
print(s1)
