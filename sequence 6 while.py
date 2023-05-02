#write a program that takes a list of integers as input and outputs the largest integer in the list usiing while loop
a=[1,2,3,4,5,6,7,9,8]
a.sort()
i=0
b=[]
while i<len(a):
    b.append(a[-1])
    i+=1
s=set(b)
print(s)
