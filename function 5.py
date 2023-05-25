#write a program that takes a list of words as input and finds the first word with more than five characters using a for loop and a break statement
def sample():
    for i in range (1,11):
        a=input("enter a name:")
        if len(a)>=5:
            break
        print(a)
sample()