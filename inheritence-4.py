# 5) Create a parent class called "Animal" with attributes "species" and "legs". Create a child class called "Cat" that inherits from "Animal" and has an additional attribute "color".

class animal:
    species="abcd"
    legs=4
    def dis_species(self):
        print(self.species)
    def dis_leg(self):
        print(self.legs)
class cat(animal):
    color="black"
    def dis_clr(self):
        print(self.color)
a=cat()
a.dis_species()
a.dis_leg()
a.dis_clr()