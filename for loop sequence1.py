#write a program to find the second largest element in a given list using a for loop
l=[1,3,66,3,44]
for i in l:
    l.sort()
    a=(l[-2])
print(a)