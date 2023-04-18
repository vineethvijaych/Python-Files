t=(5,3,"apple","orange",21)
#add an item to the second position of the tuple
a=list(t)
print(a)
a.insert(2,5)
print(a)
t=a
print(tuple(t))
#find the length of the tuple
print(len(t))
#search if 21 is present in the tuple
print(21 in t)
#reverse the tuple
b=list(t)
print(b[::-1])
print(t[::-1])
#convert a string "python" into tuple
d="python"
print(tuple(d))
