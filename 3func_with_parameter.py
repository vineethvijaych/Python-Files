#Write a function called reverse_string that takes a string as an argument and returns the reverse of that string.
a=input("enter a word:")
def reverse_string(a):
    reverse_string=a[::-1]
    print(reverse_string)
reverse_string(a)