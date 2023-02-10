class Sirsha:

    brand = "Unique :)" # Class namespace

    ''' def __init__(self):
        print("I am under __init__(), in order to use it you have to use double underscore both the time")
    '''
    def __init__(self):
        self.cpu = "i7"     # instance name
    def config():
        print("This is under config")



com1 = Sirsha()
com1.cpu = "i7" # This is how we can enter the calue in a object
print(type(com1))
com2 = Sirsha()
com2.cpu = "i9"
# print(com1)
# print(com2)

# Object
# Knows anything - attributes
# Does something - methods (functions)
print(com1.cpu)
print(com2.cpu)

Sirsha.config()
print("My brand is", Sirsha.brand)

'''
class A:
    pass
This is how we make objects and we can make classes.
We can use multiple classes in python

class B:
    pass
'''
