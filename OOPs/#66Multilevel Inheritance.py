class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def info(self):
        print(f"name is {self.name}")
        print(f"species is {self.species}")

class dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    def info(self):
        Animal.info(self)
        print(f"The breed is {self.breed}")

class GoldenR(dog):
    def __init__(self, name, color):
        dog.__init__(self, name, breed="GoldenR")
        self.color = color
    def info(self):
        dog.info(self)
        print(f"The color is {self.color}")

a = GoldenR("abc", "Black")
a.info()
print(GoldenR.mro())