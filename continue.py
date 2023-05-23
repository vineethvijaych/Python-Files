#odd numbers
for i in range(1,11):
    if i%2==0:
        continue   
    print(i)

#even numbers
for i in range(1,11):
    if i%2==1:
        continue   
    print(i)
    
a=['apple','grape','orange','car','bus']
b=['apple','grape','orange']
for i in a:
    if i not in b:
        continue
    print(i)
    
a=['apple','grape','orange','car','bus']
b=['apple','grape','orange']
for i in a:
    if i in b:
        continue
    print(i)
    


