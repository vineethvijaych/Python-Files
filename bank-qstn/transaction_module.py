class Bank: 
    n1="vineeth"
    ac1=9
    b=500
    def balance(self):
        print(self.b)
    def deposit(self,a):
        self.b+=a
        print(self.b)
    def withdraw(self,c):
        self.b-=c
        print(self.b)
v=Bank()