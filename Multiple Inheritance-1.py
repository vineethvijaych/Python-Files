# 1) Create a class Animal with a constructor that takes a name argument and stores it in an instance variable. Create a class CanFly with a method fly() that doesn't do anything. Create a class CanSwim with a method swim() that doesn't  do anything. Create a subclass Duck that inherits from Animal, CanFly, and CanSwim and has a constructor that takes a color argument and stores it in an instance variable.

class Animal:
    def __init__(self,name):
        self.name=name
class CanFly:
    def fly(self):
        pass
class CanSwim:
    def swim(self):
        pass
    def canswim(self):
        pass
class duck(Animal,CanFly,CanSwim):
    def __init__(self,color):
        self.color=color
    def dis_color(self):
        print(self.color)
    
a=duck("red")
a.dis_color()