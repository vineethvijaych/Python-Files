#Create a function called calculate_average that takes a list of numbers as an argument and returns the average of those numbers
b=[]

for i in range(1,11):
    a=int(input("enter number(use '0'to stop):"))
    if a==0:
        break
    b.append(a)
    print(b)

def avg(b):
    avg=sum(b)/len(b)
    print(avg)
avg(b)
    