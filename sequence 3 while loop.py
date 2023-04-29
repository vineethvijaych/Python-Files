#write a program that takes two list of integers as input and returns a list containing the common elements using while loop 

a=[1,2,3,4,5,6,7,8,9]
b=[2,4,6,8]
i=0
c=[]
while i<len(a):
    if a[i] in b:
        c.append(a[i])
    i+=1
print(c)
