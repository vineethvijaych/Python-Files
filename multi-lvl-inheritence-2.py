# 2) Create a class Shape with a constructor that takes a color argument and stores it in an instance variable. Create a subclass Rectangle that inherits from Shape and has a constructor that takes width and height arguments and stores  them in instance variables. Create a subclass Square that inherits from Rectangle and has a constructor that takes a side argument and sets the width and height instance variables to the value of side.

class shape:
    def __init__(self,color):
        self.color=color
    def dis_color(self):
        print(self.color)
class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def dis_width(self):
        print(self.width)
    def dis_height(self):
        print(self.height)
class square(rectangle):
    def __init__(self,width1,height1):
        self.width1=width1
        self.height1=height1
    def diswidth(self):
        print(self.width1)
    def disheight(self):
        print(self.height1)
      
a=shape("red")
b=rectangle(10,20)
c=square(40,50)
a.dis_color()
b.dis_width()
b.dis_height()
c.disheight()
c.diswidth()
