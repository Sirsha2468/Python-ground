# List comprehension
# ls = [i for i in range (1, 100) if i % 3 == 0]
# print(ls);
# ls = [];
# for i in range(1, 100):
#     if(i % 3 == 0):
#         ls.append(i);
# print(ls);

# list = [22, 11, 24, 34, 33, 56]
# ls = [i for i in (list) if i % 2 == 0]
# print(ls);

# list = [22, 11, 24, 34, 33, 56]
# ls = []
# for i in list:
#     if(i % 2 == 0):
#         ls.append(i)
# print(ls)

# d = dict();
# for i in range(1, 10):
#     d[i] = i ** 2;
# print(d);

# od = {'Jack': 38, 'Michale': 48, 'Hello': 55}; # Dictionary
# # for value in d.items():
# #     if(value % 2 == 0 and value > 40):
# #         print(value)
# d = {k : v for (k, v) in od.items() if v % 2 != 0 and v > 40}
# print(d)

# def name:
#     print("Sirsha");
# name();
# def my_function():
#   print("Hello, I am Sirsha")

# my_function();
# def add():
#     a = 10
#     b = 10
#     c = a + b
#     print(c)
# add();

# def sum(list):
#     sum = 0;
#     for i in list:
#         sum += i;
#     print(sum);
# list = [8, 2, 3, 0, 7];
# sum(list)

# def sum(list):
#     sum = 1;
#     for i in list:
#         sum *= i;
#     print(sum);
# list = [8, 2, 3, -1, 7, 8];
# sum(list)

# def check(n):
#     if n in range(3, 15):
#         print("Present");
#     else:
#         print("Not present");
# n = eval(input("Enter a number:"))
# check(n);
def Check_UL(string):
    count1 = 0;
    count2 = 0;
    for i in string:
        if(i.isupper()):
            count1 = count1 + 1;
        elif(i.islower()):
            count2 = count2 + 1;
    print("Number of upper case: ", count1);
    print("Number of lower case: ", count2);
string = input("Enter any string: ")
Check_UL(string);
