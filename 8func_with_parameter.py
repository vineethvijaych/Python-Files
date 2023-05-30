#write a function called 'check palindrome ' that takes a string as an argument and returns 'true' if the string is a palindrome (reads the same forwads and backwards) and 'false' otherwise
a=input("enter a word:")
b=[]
def check_palindrome(a):
    if a==a[::-1]:
        print("true")
    else:
        print("false")    
    
check_palindrome(a)

check_palindrome("man")
check_palindrome("eye")