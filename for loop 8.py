#write a program to find the factorial of a given number using a for loop
a=int(input("enetr a number:"))
fact=1
for i in range (1,a+1):
    fact*=i
print(fact)
