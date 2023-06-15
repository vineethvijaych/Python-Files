a=10
b=0
d=5
print(a+d)

try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("division by zero") 
    print("program continue...") 
else:
    print('no error found') 
finally:
    print('python')
    
print(a-d)