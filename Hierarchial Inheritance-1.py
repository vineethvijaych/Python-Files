# 1) Create a class Vehicle with instance variables brand and model, and a method start_engine() that prints a message that the engine has started. Create a class Car that also inherits from Vehicle and has additional instance  variables color and seats, and a method drive() that prints a message that the car is being driven. Create a class Bike that also inherits from Vehicle and has additional instance variables color and type, and a method ride()  that prints a message that the bike is being ridden. Create objects of both Car and Bike classes and call their respective methods.

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def start_engine(self):
        print("engine has started")
class Car(Vehicle):
    def __init__(self,color,seats):
        self.color=color
        self.seats=seats
    def drive(self):
        print("the car is being driven")
class Bike(Vehicle):
    def __init__(self,color,type):
        self.color=color
        self.type=type
    def ride(self):
        print("the bike is being ridden")
        
a=Vehicle("honda","cbr")
a.start_engine()
b=Car("red",7)
b.drive()
c=Bike("green","superbike")
c.ride()
    