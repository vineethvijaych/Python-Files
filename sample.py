# a=input ("user name:")
# print("welcome "+a)
# a="i like chocolates,chocolates are my favorate"
# b="chocolate"
# print(a.count('chocolates'))

c=[10,11,85,1,3,11,2,11]
#interchange the first elelment with the last element
d=len(c)
print(d)
p=(c[-1])
c[-1]=c[0]
print(c)
d=c[0]
c[0]=p
print(c)
#length
print(len(c))
#find the number of occurance of 11 in the list
print(c.count(11))
#make a clone of this list
d=c
print(d)
print(c)
#add an item to the third position(index)of the list
c.insert(3,22)
print(c)
#sum
print(sum(c))
#sort 
c.sort()
print(c)
#reverse the list
print(c[::-1])



