# Write a Python program that reads a list of numbers from user input and calculates the sum. Handle the ValueError exception if the user enters a non-numeric value, and continue reading numbers until the user enters "done". Then, display the sum of the numbers.
try:
    b=[]
    for i in range (1,5):
        a=int(input("enter number:"))
        b.append(a)
    print(b)
except:
    print("ValueError: invalid literal")
else:
    print("input accepted")
finally:
    print("program continue...")