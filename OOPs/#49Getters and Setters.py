class Myclass:
    def __init__(self, value):
        self.value = value
    def info(self):
        print(f"The value is {self.value}")
    @property
    def ten_value(self):
        return 10*self.value
    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value/10
    
obj = Myclass(10)
obj.ten_value = 78
print(obj.ten_value)
obj.info()