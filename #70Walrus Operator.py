# a = True
# print(a=False) ----> will give an error
a = True
print(a:=False)

#ye he aam jindagi
food = list()
while True:
    a = input("Enter the food name")
    if a=="quite":
        break
    food.append(a)

#ye he mentos jindagi
food = list()
while a:=input("Enter the food name") != "quite":
    food.append(a)