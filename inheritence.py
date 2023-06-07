#1) Create a parent class called "Vehicle" with a method "start_engine" that prints out "The engine is starting". Create a child class called "Car" that inherits from "Vehicle" and has an additional method "drive" that prints out "The car is driving".

class vehicle:
    def start_engine(self):
        print("engine is starting")
class car(vehicle):
    def drive(self):
        print("the car is driving")
a=car()
a.start_engine()
a.drive()