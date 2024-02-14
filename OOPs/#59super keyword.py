# class ParentClass:
#     def parent_method(self):
#         print("I am inside parent method")

# class Childclass(ParentClass):
#     def parent_method(self):
#         print("Hello")
#         super().parent_method()
    
#     def child_method(self):
#         print("I am inside the child method")
#         super().parent_method()

# child_obj = Childclass()
# child_obj.child_method()
# child_obj.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def info(self):
        print(f"name is {self.name} and id is {self.id}")

class programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
    def info(self):
        super().info()
        print(f"and language is {self.lang}")

a = Employee("Om", 65)
b = programmer("Vin", 38, "python")
a.info()
b.info()