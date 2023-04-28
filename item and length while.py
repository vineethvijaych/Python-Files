l=['python','apple','orange','grape']
i=0
a={}
while i<len(l):
   
    a.update({l[i]:len(l[i])})
    
    i+=1
print(a)
