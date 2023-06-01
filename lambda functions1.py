#create a list of numbers [1,2,3,4,5] and use a lambda function to filter out the even numbers from the list
# b=[]
# for i in range (1,6):
#     b.append(i)
# x=lambda a:a%2==0
# print(x(b))
    


l=[1,2,3,4,5]
var = filter(lambda i:i%2==0,l)
print(var)
for j in var:
    print(j)
    