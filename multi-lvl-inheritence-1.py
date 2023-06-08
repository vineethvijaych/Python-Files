# 1) Create a class Person with a constructor that takes a name and age argument and stores them in instance variables. Create a subclass Employee that inherits from Person and has a constructor that takes a salary argument and stores  it in an instance variable. Create a subclass Manager that inherits from Employee and has a constructor that takes a department argument and stores it in an instance variable.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis_name(self):
        print(self.name)
    def dis_age(self):
        print(self.age)
class employee(person):
    def __init__(self,salary):
        self.salary=salary
    def dis_salary(self):
        print(self.salary)
class manager(employee):
    
    def __init__(self,department):
        self.department=department
    def dis_department(self):
        print(self.department)

p=person("vineeth",22)
d=manager("accounts")
a=employee(1500)

d.dis_department()
p.dis_name()
p.dis_age()
a.dis_salary()




