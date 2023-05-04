# write a program to find the greatest common divisor (GCD) of two number using a fpr loop
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=[]
d=[]
e=[]
for i in range(1,20):
    if a%i==0:
        c.append(i)
for i in range(1,20):
    if b%i==0:
        d.append(i)
for i in range(1,20):
    if c[i]==d[i]:
        e.append(i)
        
print(c)
print(d)      
print(e)
