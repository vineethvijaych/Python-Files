# Write a Python function that takes a list of numbers as input and returns the mean (average) of those numbers using the math module.

from statistics import median,mean

b=[]
for i in range(1,6):
    a=input("enter a number:")
    b.append(i)
print(b)
print(mean(b))

