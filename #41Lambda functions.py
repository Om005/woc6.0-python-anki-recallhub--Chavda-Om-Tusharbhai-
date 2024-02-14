def func(fx, value):
    return 10+fx(value)

# def double(n):
#     return n*2
double = lambda x: 2*x
cube = lambda x: x**3   
average = lambda x, y: (x+y)/2
print(double(3))

print(func(cube, 4))