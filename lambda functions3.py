#write a lambda function that checks whether a given number is divisible by 3
# a=[1,2,3,4,5,6,7,8,9]
# x=filter(lambda i:i%3==0,a)
# print(x)
# for j in x:
#     print(j)

a=int(input("enter number:"))
x=lambda i:i%3==0
print(x(a))
