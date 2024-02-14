a = int(input("enter a numer between 5 and 9:"))
if(a<5 or a>9):
    raise ValueError("Invaid input number should be between 5 and 9")

b = input("Enter a string:")
if(b!="quite"):
    raise ValueError("Invalid string.")