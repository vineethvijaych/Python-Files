#write a function named "calculate area" that takes two parameters, 'length' and 'width' , and returns the area of a rectangle
a=int(input("length:"))
b=int(input("width:"))
def calculate_area(a,b):
    calculate_area=a*b
    return calculate_area
print(calculate_area(a,b))