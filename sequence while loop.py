# a=str(input("enter subject:"))

# a.split(",")
# print(list(a))
#write a program that takes a list of strings as input and outputs the length of each string using while loop
b=input("enter a name:")
c=input("enter name 2:")
d=input("enter name 3:")
e=[]
e.append(b)
e.append(c)
e.append(d)

i=0
while i<len(e):
    print(e[i],len(e[i]))
    i+=1

    