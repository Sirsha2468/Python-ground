Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l1 = [2, 4, 6, 8]
hash(l1)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    hash(l1)
TypeError: unhashable type: 'list'
y = 4.8
type(y)
<class 'float'>
hash(y)
1844674407370954756
l1
[2, 4, 6, 8]
hash(l1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    hash(l1)
TypeError: unhashable type: 'list'
#unhashable type: 'list'
print("unhashable type: 'list'")
unhashable type: 'list'
"Teacher's day"
"Teacher's day"
print("\"Teacher's Day"\")
SyntaxError: unexpected character after line continuation character
print("\"Teacher's Day\"")
"Teacher's Day"
print('''"Teacher's Day"''')
"Teacher's Day"
while i < len(s1):
    print(s1[i])
    i+=1

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    while i < len(s1):
NameError: name 'i' is not defined. Did you mean: 'id'?
i = 0
while i < len(s1):
    print(s1[i])
    i+=1

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    while i < len(s1):
NameError: name 's1' is not defined. Did you mean: 'l1'?
s1 = "Hello"
while i < len(s1):
    print(s1[i])
    i+=1

H
e
l
l
o
r = range[5]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    r = range[5]
TypeError: 'type' object is not subscriptable
r[0]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    r[0]
NameError: name 'r' is not defined
s1 = "Sirsha Dey"
min(s1)
' '
sum(s1)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sum(s1)
TypeError: unsupported operand type(s) for +: 'int' and 'str'

= RESTART: C:/Users/Admin/Desktop/Program/Python/Sum of n natural number_ 2.py
Enter a number: 
5
15

= RESTART: C:/Users/Admin/Desktop/Program/Python/Sum of n natural number_ 2.py
Enter a number: 
3
6
s2 = "2468"
sum(list(s2))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    sum(list(s2))
TypeError: unsupported operand type(s) for +: 'int' and 'str'

=========== RESTART: C:/Users/Admin/Desktop/Program/Python/Str.py ===========
5
5

=========== RESTART: C:/Users/Admin/Desktop/Program/Python/Str.py ===========

=========== RESTART: C:/Users/Admin/Desktop/Program/Python/Str.py ===========
sum([int(e) for e in s2 if ord(e) >= 49 and ord(e) <= 57])
10
s1 = "Sirsha Dey"
sorted(s1)
[' ', 'D', 'S', 'a', 'e', 'h', 'i', 'r', 's', 'y']
s1.index('e')
8
s1.index('E')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s1.index('E')
ValueError: substring not found
s1
'Sirsha Dey'
s1.count
<built-in method count of str object at 0x0000029C90E12DB0>
s1.count('e')
1
s1.count('s')
1
s1.count('Sirsha')
1
s1.count(' ')
1
s1.startwith("Sir")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s1.startwith("Sir")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
yes
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
s1.startswith("Sir")
True
s1.alnum()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s1.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
s1.isalnum()
False
s1.isalpha()
False
s1.isdigit()
False
s1.isalpha()
False
s2 = "Hello"
s2.isalpha()
True
print("True because there is no space in Hello")
True because there is no space in Hello
s2.isupper()
False
s2.islower()
False

========== RESTART: C:/Users/Admin/Desktop/Program/Python/Format.py =========

========== RESTART: C:/Users/Admin/Desktop/Program/Python/Format.py =========
{}, Welcome
s1 = "{}, Welcome"
s1.format("Sirsha")


========== RESTART: C:/Users/Admin/Desktop/Program/Python/Split.py ==========
Enter number separated by comma

========== RESTART: C:/Users/Admin/Desktop/Program/Python/Split.py ==========
Enter number separated by comma
2, 4, 6
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Program/Python/Split.py", line 2, in <module>
    l1 = [int(e) for e in input().split('')]
ValueError: empty separator
2,4,6
(2, 4, 6)

========== RESTART: C:/Users/Admin/Desktop/Program/Python/Split.py ==========
Enter number separated by comma
2,4,6
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Program/Python/Split.py", line 2, in <module>
    l1 = [int(e) for e in input().split('')]
ValueError: empty separator

========== RESTART: C:/Users/Admin/Desktop/Program/Python/Split.py ==========
Enter number separated by comma
2,4
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Program/Python/Split.py", line 2, in <module>
    l1 = [int(e) for e in input().split('')]
ValueError: empty separator

========== RESTART: C:/Users/Admin/Desktop/Program/Python/Split.py ==========
Enter number separated by comma
3, 4
[3, 4]

========== RESTART: C:/Users/Admin/Desktop/Program/Python/Split.py ==========
Enter number separated by comma
3 4
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Program/Python/Split.py", line 2, in <module>
    l1 = [int(e) for e in input().split(',')]
  File "C:/Users/Admin/Desktop/Program/Python/Split.py", line 2, in <listcomp>
    l1 = [int(e) for e in input().split(',')]
ValueError: invalid literal for int() with base 10: '3 4'
l1
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    l1
NameError: name 'l1' is not defined
s1
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s1
NameError: name 's1' is not defined

s1 = "How are you"
print(s1)
How are you
s1
'How are you'
s1[1:10:2]
'o r o'
s1[10:5:-1]
'uoy e'
s1[:5:1]
'How a'
s1[20:]
''
s1[8:]
'you'
s1[::-1]
'uoy era woH'
