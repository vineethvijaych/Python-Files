# write a program to check if given number is prime or not, using a for loop
a=int(input("enter a number:"))
for i in range (1,a):
    if (a%i==0):
        print('prime number')
    else:
        print("not a prime number")
