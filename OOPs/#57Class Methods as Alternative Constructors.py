class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(self, str):
        return self(str.split("-")[0], int(str.split("-")[1]))
    def info(self):
        print(f"name is {self.name} and salary is {self.salary}")

a = Employee("om", 101010101010010010)
a.info()
b = Employee.fromstr("Vin-12")
b.info()