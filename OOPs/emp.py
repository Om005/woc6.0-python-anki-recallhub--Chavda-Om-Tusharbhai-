class Employee:
    def __init__(self, name):
        self.name = name
    
    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    def __repr__(self):
        return f"The name of the employee is {self.name} repr"

    def __call__(self):
        print("Hey hey hey everybody hey")