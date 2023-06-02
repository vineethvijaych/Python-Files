class person:
    a = 10
    name="vineeth"
    def display(self,b):
        self.b=b
        sum = self.a+b
        print(sum) 
        print(self.name)

    def sample(self):
        s = self.a+self.b
        print(s)
    

obj = person()  
obj.display(20) 
obj.sample()
