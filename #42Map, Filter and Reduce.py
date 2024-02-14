#---------MAP---------------
def cube(n):
    return n**3

l = [1, 2, 3, 4, 5, 6]
# newl =[]
# for item in l:
#     newl.append(cube(item))
newl = list(map(cube, l))
newl = list(map(lambda x: x**3, l))
print(newl)

#---------filter------------
def filter_function(a):
    return a>4
newnewl = list(filter(filter_function, l))
print(newnewl)


#----------reduce---------
from functools import reduce
sum = int(reduce(lambda x,y: x+y, l))
mul = int(reduce(lambda x,y: x*y, l))
print(sum)
print(mul)