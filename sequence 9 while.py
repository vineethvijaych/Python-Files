#write a program that takes a list of integers as input and outputs a new list containing only the even integers using while loop
a=[1,2,3,4,5,6,7,8,9]
i=0
b=[]
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
    i+=1
print(b)