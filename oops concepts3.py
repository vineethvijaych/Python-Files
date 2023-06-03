# 2. Create a Person class with attributes name and age. Implement a method is_major() that returns True if the person is 18 years or older, and False otherwise. 
class person:
    name="vineeth"
    age=22
    def major(self):
        if self.age>=18:
            print("true")
        else:
            print("false")
obj=person()
obj.major()
        

