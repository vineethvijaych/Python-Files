print("hello\n""hello\n""hello\n""hello") 
print("hello\n"*5)
#initialization
a=1
while a<11:
    print("hello")
    a+=1
b=1
while b<11:
    if b%2==0:
        print(b)
    b+=1
####
#write a program to print both even and odd numbers in between tow numbers given by user
c=int(input("enter number 1:"))
d=int(input("enter number 2:"))
e=c
while e<=d:
    print(e)
    e+=1
####
#print both even and odd numbers in between 1 and 10 as list
g=[]
h=[]
f=1
while f<11:
    if f%2==0:
         g.append(f)
    else:
        h.append(f)
    f+=1     
print(h)      
print(g) 
   
    
   
   