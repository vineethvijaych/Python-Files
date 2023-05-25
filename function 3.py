#write a program that takes input from the user and stops taking input when the user enters "stop"
def sample():
    for i in range(1,11):
        a=input("enter a word:")
        if a=='stop':
            break
        print(a)
sample()
    
