# Implement a function that calculates the square root of a given number using the math module. Handle cases where the input is negative and return an appropriate message.
import math as m
a=int(input("enter a number:"))
print((m.sqrt(m.fabs(a))))