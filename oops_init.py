class sample:
    def __init__(self,a,b,c):
        self.a=a
        self.b =b
        self.c =c

    def add(self):
        sum = self.a+self.b+self.c
        print(sum)
    def mult(self): 
        m = self.a*self.b*self.c
        print(m)

o = sample(3,4,5)
o.add()
o.mult()