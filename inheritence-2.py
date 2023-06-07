# 3) Create a parent class called "Shape" with attributes "color" and "size". Create a child class called "Circle" that inherits from "Shape" and has an additional attribute "radius".

class shape:
    color=input("color:")
    size=input("size:")
    def clr(self):
        print(self.color)
    def dis_size(self):
        print(self.size)
class circle(shape):
    radius="30cm"
    def dis_radius(self):
        print(self.radius)
a=circle()
a.clr()
a.dis_size()
a.dis_radius()