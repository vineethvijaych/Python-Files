#write a program that takes list of strings as input and outputs a new list containing only the strings with more than five charecters using a while loop
a=["apple","mango","orange","grapes"]
i=0
while i<len(a):
    if len(a[i])>5:
        print(a[i])
    i+=1
