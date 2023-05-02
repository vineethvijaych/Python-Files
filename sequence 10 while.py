#write a program that takes a list of string as input and outputs a new list containing the same strings,but with the first letter capitalized using a while loop
a=["apple","mango","orange","grapes"]
i=0
b=[]
while i<len(a):
    b.append(a[i].capitalize())
    i+=1
print(b)