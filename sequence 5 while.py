#write a program that takes a list of integers as inputs and outputs the sum of the integers using while loop
a=[1,2,3,4,5,6,7,8,9]
b=0
sum=0
while b<len(a):
    sum += a[b]
    
    b+=1
print(sum)   