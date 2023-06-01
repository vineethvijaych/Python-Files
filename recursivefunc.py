# def display():
#     sum=10+20
#     print(sum)
#     print('hello')
#     display()
# display() 

def fact(n):
    if n==1:
        return n
    else:
        return n * fact(n-1)
print(fact(5))
    