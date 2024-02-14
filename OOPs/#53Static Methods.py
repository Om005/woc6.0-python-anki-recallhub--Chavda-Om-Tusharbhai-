class Math:
    def __init__(self, num):
        self.num = num
    def addtonum(self, n):
        return self.num+n
    
    @staticmethod
    def sum(a, b):
        return a+b
    
print(Math.sum(3, 4))
a = Math(4)
print(a.addtonum(4))
print(a.sum(56, 67))