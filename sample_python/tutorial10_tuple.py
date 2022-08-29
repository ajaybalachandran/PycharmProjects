# myCars is a tuple values in a tuple cannot be replaced directly
myCars = ('bmw', 'audi', 'toyota')
print(type(myCars))
print(myCars)

# converting myCars tuple into a list and then change values and then convert it back to tuple
myCars_temp = list(myCars)
print(type(myCars_temp))
print(myCars_temp)
myCars_temp[0] = 'alto'
myCars = tuple(myCars_temp)
print(myCars)
