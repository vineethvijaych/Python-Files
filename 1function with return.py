#define a function called 'find maximum' that takes a list of numbers as an argument and returns the largest number in the list 
b=[]
for i in range(1,11):
    a=int(input("enter number(use '0'to stop):"))
    if a==0:
        break
    b.append(a)
    print(b)
def find_maximum(a):
    find_maximum=max(a)
    return find_maximum
print(find_maximum(b))