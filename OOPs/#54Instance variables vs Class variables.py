class Employee:
    companyname = "Google" #----->This is class variable
    def __init__(self, name, n):
        self.name = name      # This is instance variable
        self.raise_amount = n # This is instance variable 
    def info(self):
        print(f"The raise amount of the employee {self.name} of company {self.companyname} is {self.raise_amount}")

a = Employee("kri", 0.2) 
a.companyname = "Microsoft" #---> This is a instance variable 
#--> So when companyname comes firstly it will be searched in instance variable
#--> Here we defind a instance variable companyname in employee a so it will be printed instead of class variable
a.info()
Employee.companyname = "Nestle"
#>> class variable changed
b = Employee("Om", 0.12) 
b.info()