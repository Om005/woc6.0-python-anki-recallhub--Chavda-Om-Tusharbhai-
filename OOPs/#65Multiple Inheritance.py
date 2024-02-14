class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def info(self):
        print(f"The dance is {self.dance}")

        
class dancerperson(Person, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

a = dancerperson("abc", "kathak")
print(a.name)
print(a.dance)
a.info()#----->Firstly find in Person class then find in Dancer(if not found in Person)

print(dancerperson.mro())