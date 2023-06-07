# 4) Create a parent class called "Person" with attributes "name" and "age". Create a child class called "Student" that inherits from "Person" and has an additional attribute "grade".

class person:
    name="vineeth"
    age=22
    def dis_name(self):
        print("name:",self.name)
    def dis_age(self):
        print("age:",self.age)
class student(person):
    grade="A"
    def dis_grade(self):
        print("grade:",self.grade)
a=student()
a.dis_name()
a.dis_age()
a.dis_grade()