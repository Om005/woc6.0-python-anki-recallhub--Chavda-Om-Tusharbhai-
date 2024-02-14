class Employee:
    company = "Apple"
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def chagecompany(ookrrrrr, new):
        ookrrrrr.company = new

e1 = Employee("Om")
e1.info() 
e1.chagecompany("Tesla")
e1.info() 
e2 = Employee("Vin")
e2.info() 