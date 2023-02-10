class Student:

    school = "RKVM"
    
    def __init__(self):
        self.marks = 10

    def get_marks(self):
        return self.marks

    def get_school():
        return cls.school #cls is representing class

s1 = Student()
s2 = Student()

print(s1.marks)
#print(Student.school)
print(s1.get_school)

