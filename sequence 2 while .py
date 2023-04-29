#write a program that takes a string as input and outputs the number of times each charecter appears in the string using awhile loop
a="apple","orange","grapes","apple"
i=0
b={}
while i<len(a):
    a1=(a[i],a.count(a[i]))
    if a[i] not in b:
        b.update({a[i]:a.count(a[i])})
       
    i+=1  
print(b)

