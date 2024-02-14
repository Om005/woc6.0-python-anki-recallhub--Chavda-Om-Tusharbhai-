class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def info(self):
        print(f"The name of employee id {self.id} is {self.name}")

a = Employee("abc", 332)
a.info()

class programmer(Employee):
    def showlanguage(self):
        print("The default language is python.")

b = programmer("OM", 334)
b.info()
b.showlanguage()