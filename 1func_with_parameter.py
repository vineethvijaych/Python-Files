a=int(input("number1:"))
b=int(input("number2:"))
def sum(a,b):
    sum =a+b
    print(sum)
def sub(a,b):
    sub =a-b
    print(sub)
def div(a,b):
    div=a/b
    print(div)
def multi(a,b):
    multi=a*b
    print(multi)
print("operators:+,-,/,*")
c=input("operation:")  
if c=='+':
    sum(a,b)
elif c=='-':
    sub(a,b)  
elif c=='/':
    div(a,b)
elif c=='*':
    multi(a,b)

    