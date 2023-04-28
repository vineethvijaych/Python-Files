a=['apple',2,'orange',4,5]
print(type(a))
i=0
c=0
while i<len(a):
    # print(a[i])
    # print(type(a[i]))
    if type(a[i])==str:
        print(a[i])
    i+=1        