# create function called 'count_vowels' that takes astring as an argument and returns the number of vowels in the string
st=input("enter name:")
a=["a","e","i","o","u"]
def count_vowels(a):
    i=0
    c=0
    while i<len(st):
        if st[i] in a:
            c+=1
        i+=1
    count_vowels=print(c)
print(count_vowels)
count_vowels(a)    
