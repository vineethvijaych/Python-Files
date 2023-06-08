# 3) Create a class Person that has instance variables name and age, and a method speak() that prints a message indicating that the person is speaking. Create subclasses Student and Teacher that inherit from Person and add a method  study() to Student and a method teach() to Teacher. Create objects of the Student and Teacher classes and call their speak(), study(), and teach() methods.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("the person is speaking")
class Student(Person):
    def study(self):
        print("study")
class Teacher(Person):
    def teach(self):
        print("teach")

a=Person("vineeth",22)
b=Student("adharsh",23)
c=Teacher("ashwin",24)
a.speak()
b.study()
c.teach()