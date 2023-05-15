#write a program to remove all the duplicates from a given list using a for loop
l=[1,2,2,3,4,4,5,6,7]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
        
    
    
