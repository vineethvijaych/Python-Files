#write a program that takes a list of numbers as input and stops processing the list when a negative number is encountered
def sample():
    for i in range(1,11):
        a=input("enter a word:")
        if a.startswith('-'):
            break
        print(a)
sample()
