class Person:
    name = "Vin"
    occupation = "Developer"
    networth = 2000000000
    def info(self):
        print(f"{self.name} is {self.occupation}")
a = Person()
b = Person()
a.info()

b.name = "arr"
b.occupation = "HR"
b.info()