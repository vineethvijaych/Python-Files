l=['orange',2,'grapes',4,5.8]
i=0

while i<len(l):
    if type(l[i])==int:
        a=(l[i])
        b=(type(l[i]))
        print(a,b)
    elif type(l[i])==str:
        c=(l[i])
        d=(type(l[i]))
        print(c,d) 
    elif type(l[i])==float:
        e=(l[i])
        f=(type(l[i]))
        print(e,f)   
    i+=1
    
    
i = 0
while i<len(l):
    print(l[i],type(l[i]))
    i+=1
        