class employee:
    b="hello"
    def __init__(self,name,age,salary):
        self.name=name
        self.salary=salary
        self.age=age
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age) 
    def get_salary(self):
        print(self.salary)
        
a=employee("vineeth",22,15000)
# a.get_name()
# a.get_age()
# a.get_salary()       
    
    
