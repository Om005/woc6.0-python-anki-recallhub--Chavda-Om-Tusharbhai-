class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y
    
class circle(shape):
    def __init__(self, r):
        # self.radius = r
        super().__init__(r, r)
    def area(self):
        return 3.14*super().area()
    
# rec = shape(3, 4)
# print(rec.area())
c = circle(4)
print(c.area())