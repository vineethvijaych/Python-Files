# 2) Create a class Person with a constructor that takes a name argument and stores it in an instance variable. Create a class CanCook with a method cook() that doesn't do anything. Create a class CanPaint with a method paint() that  doesn't do anything. Create a subclass Chef that inherits from Person, CanCook, and CanPaint and has a constructor that takes a specialty argument and stores it in an instance variable.

class Person:
    def __init__(self,name):
        self.name=name
class CanCook:
    def cook(self):
        pass
class CanPaint:
    def paint(self):
        pass
class chef(Person,CanCook,CanPaint):
    def __init__(self,specialty):
        self.specialty=specialty
    
        