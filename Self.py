''' def compare(s1, s2):
    if s1.marks > s2.marks:
        print("s1")
    else:
        print("S2")
'''
class Student:

    def __init__(self, marks):
        self.marks = marks
    def compare(self, other):
        if s1.marks > s2.marks:
            print("s1")
        else:
            print("S2")


s1 = Student(40)
s2 = Student(85)

s1.compare(s2)
