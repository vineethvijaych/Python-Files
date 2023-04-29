##write a program that takes a list of strings as input and outputs the length of each string using while loop
l=['word','alpha','malayalam']
i=0
a=[]
while i<len(l):
    a.append(len(l[i]))
    i+=1
print(a)