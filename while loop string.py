st="python"

a=["a","e","i","o","u"]



i = 0
c=0
while i<len(st):
    if st[i] in a:
        c+=1
    i+=1
    
print(c)