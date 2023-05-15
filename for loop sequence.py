# string
# list
# tuple
# set
# dictionary

st = 'python'

for i in st:
    print(i)
    
l = [1,2,34]
for i in l:
    print(i)

s={1,2,3,4,5}
for i in s:
    print(i)

t=("apple","orange","grape")
for i in t:
    print(i)
    
dct={'apple':'1','orange':'6','grape':'10'}
for i in dct:
    print(i,dct[i])

dct1={'apple':'1','orange':'6','grape':'10'}
for i in dct1.values():
    print(i)
