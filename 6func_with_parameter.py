#write a function named 'calculate_area' that takes the radius of a circle as an argument and returns the area of the circle 
#A=πr2
r=int(input("enter the radius:"))
def calculate_area(r):
    calculate_area=(3.14)*(r*r)
    print(calculate_area)
calculate_area(r)