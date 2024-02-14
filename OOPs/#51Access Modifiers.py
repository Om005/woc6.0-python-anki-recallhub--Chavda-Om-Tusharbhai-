class Employee:
    def __init__(self):
        self.__name = "Om" #--->This is not private but this called private
        self._id = 23
a = Employee()
# print(a.__name) -----> can not access directly, will throw an error
print(a._Employee__name) #----> but can access indirectly
# This is name mangling
print(a.__dir__())

print(a._id) #----> this is called protected but this can be access 
            # this all are only convansions there is no any private protected or public