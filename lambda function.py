x = lambda a : a + 10
print(x(5))

y=lambda a,b: a*b
print(y(10,2))

a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))

z=lambda a,b,c:a+b+c
print(z(a,b,c))

m=lambda a,b,c:a*b*c
print(m(1,2,3))

n=lambda a,b,c:a*b/c
print(n(1,6,2))

p=lambda a,b,c:a+b-c
print(p(2,8,3))
c=[]
for i in range(1,6):
    b=int(input("enter number:"))
    c.append(b)
    a=lambda 