#write a function named "power" that takes two parameters,'base' and 'exponent', and returns the result of raising the base to the exponent
a=int(input("base:"))
b=int(input("exponent:"))
def power(a,b):
    power=a**b
    return power
print(power(a,b))