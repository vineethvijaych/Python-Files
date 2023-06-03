class person:
    a="welcome "
    
    def welcome(self,b):
        self.b=b
        welcome=self.a+b
        print(welcome)
#yob=year of birth
    d=2023
    def yob(self,age):
        self.age=age
        yob=self.d-age
        print(yob)

c=input("enter name:")
e=int(input("enter age:"))
obj=person()
obj.welcome(c)
obj.yob(e)            