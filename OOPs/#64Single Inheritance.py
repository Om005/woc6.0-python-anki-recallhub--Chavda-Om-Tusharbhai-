class animal:
    def __init__(self, name, species):
        self.name = name
        self.species  = species
    def info(self):
        print(f"name is {self.name} and species is {self.species}")
class cat(animal):
    def __init__(self, name, species, hello):
        animal.__init__(self, name, species)
        hello = "meou"
    def info(self):
        print(f"name is {self.name} and species is {self.species}")

a = animal("abc", "xyz")
a.info()
b = cat("sjdl", ";;djkf", "asfdh")
b.info()