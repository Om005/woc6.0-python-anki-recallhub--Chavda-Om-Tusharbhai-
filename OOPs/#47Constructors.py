class person:
    # def __init__(self):
    #     print("Hey i am a default constructor.")
    def __init__(self, n, o):
        print("Hey i am inside the constructor.")
        self.name = n
        self.occipation = o
    def info(self):
        print(f"{self.name} is {self.occipation}")
a = person("Parth", "Developer")
b = person("Yash", "Mechenical egineer")
# c = person() -----> will throw an error
# c = person()
a.info()
b.info()