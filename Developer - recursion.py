HR = 5000
def __init__(self, name, designation,basic_salary):
        self.name = name
        self.designation = designation
        self.basic_salary = basic_salary
        
    def salary(self):
        return self.basic_salary
    def __str__(self):
        return f"{self.name} in position {self.designation} with salary {self.salary()}"
        
class Developer(Employee):
    def salary(self):
        da = (125 / 100) * self.basic_salary
        incentive = 10000
        return self.basic_salary + Employee.HR + da + incentive
        
    def __str__(self):
        return f"{self.name} in position {self.designation} with salary {self.salary()}"
class HR(Employee):
    def salary(self):
        da = (125 / 100) * self.basic_salary
        return self.basic_salary + Employee.HR + da
    def __str__(self):
        return f"{self.name} in position {self.designation} with salary {self.salary()}"
        
hello = Developer("hello", "SCE", 68415)
Here = HR("Here", "HR", 50000)
print(hello)
print(Here)
