#write a function called 'is_even_odd' that takes a number as an argument abd returns "even" if the number is even , and "odd" if teh number is odd
a=int(input("enter a number:"))

def is_even_odd(a):
    if a%2==0:
        print("even")
    else:
        print("odd")    
    
is_even_odd(a)
