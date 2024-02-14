#------dir-------
lst = [1, 3, 5]
tup = (1, 3, 5)
print(dir(lst))
# print(lst.__add__)

#--------__dict__-----> self. vala will be printed
class Person:
    version = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
a = Person("Om", 17)
print(a.__dict__)

#----help---
# print(help(str))