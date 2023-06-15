# Write a Python program that asks the user to enter their age. Handle the ValueError exception if the user enters a non-numeric value, and display an appropriate error message.

try:
    a=int(input("enter your age:"))
    print(a)
except:
    print("invalid literal for int()")
    
else:
    print("input accepted")
finally:
    print("program continue...")