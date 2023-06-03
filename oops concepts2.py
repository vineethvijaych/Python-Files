# #1. Create a Rectangle class with attributes length and width. Implement a method calculate_area() that calculates and returns the area of the rectangle. 

class rectangle:
    length=int(input("length:"))
    width=int(input("width:"))
    def calculate_area(self):
        area=self.length*self.width
        print(area)
obj=rectangle()
obj.calculate_area()