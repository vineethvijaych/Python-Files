#given a list of integers [1,2,3,4,5],use a lambda function to calculate the square of each number and store the result in a new list.
# a=[1,2,3,4,5]
# x=lambda b:b**2
# for i in (a):
#     print(x(a[i]))

a=[1,2,3,4,5]
x=filter(lambda b:b**2,a)
print(x)
for i in x:
    print(i)