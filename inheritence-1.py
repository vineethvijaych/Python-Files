# 2) Create a parent class called "Employee" with attributes "name" and "salary". Create a child class called "Manager" that inherits from "Employee" and has an additional attribute "department".

class employee:
    name="vineeth"
    salary=15000
    def disname(self):
        print("name is",self.name)
    def dissalary(self):
        print(self.salary)
class manager(employee):
    department="accounts"
    def depart(self):
        print(self.department)
a=manager()
a.disname()
a.dissalary()
a.depart() 


