def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx
        

@greet
def hello():
    print("Hello world")
@greet
def sum(a, b):
    print(a+b)
# greet(hello)()
hello()

sum(1,2)
# greet(sum)(1, 2)