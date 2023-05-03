#input 2 numbers fromuser and make calculations by the instruction given by the user (*,+,-,/)
b="1.add(+)\n2.sub(-)\n3.div(/)\n4.multi(*) "
print(b)
sum=0
sub=0
multi=1
c=[]
# c=input("enter operation:")
for i in range(1,3):
    a=int(input("enter number:"))
    c.append(a)
    sum+=a
    sub-=a
  
    multi*=a
b=input("operation:")
if b=="+":
    print(sum)
elif b=="-":
    print(sub)
elif b=="/":
    print(c[0]/c[1])
elif b=="*":
    print(multi)
    



    
    
