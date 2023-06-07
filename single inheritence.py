class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disname(self):
        print(self.name)
    def disage(self):
        print(self.age)

class employee(person):
    def dis_salary(self,salary):
        print(salary)
        print(self.dep)

b=employee("vineeth",22)
b.dis_salary(15000)
b.disname()
b.disage()
