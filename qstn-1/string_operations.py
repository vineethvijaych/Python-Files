# 2. Create a module named "string_operations" which contains the following functions: 
#  reverse_string(string): Returns the reversed string 
#  count_vowels(string): Returns the count of vowels in the given string
# Import the module in a separate Python script and use the functions to perform some string operations.

def reverse_string(a):
    print(a[::-1])
v=('a','e','i','o','u')  
d=[]
def count_vowels(b):
    for i in b:
       if i in v:
           d.append(i)
    print(d) 
    print("count:",len(d))
    

    
    
    
