#given a list of string ["apple","banana","dates","cherry"], use a lambda function to sort the list in alphebetical order
a=["apple","banana","dates","cherry"]
b=filter(lambda i:i.sort(),a)
print(b)
for j in b:
    print(j)

