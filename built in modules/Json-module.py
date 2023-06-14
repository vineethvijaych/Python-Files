import json as j

#converting to python

a='{"name":"abc","age":22}'
c=(j.loads(a))
print(type(c))
print(c)

#converting  string to json

b="vineeth123"
d=(j.dumps(b))
print(d)
print(type(d))

#set can not be converted to json so we have to change its format to list by typecasting

e={1,2,3,4,5}
m=list(e)
n=(j.dumps(m))
print(n)
print(type(n))