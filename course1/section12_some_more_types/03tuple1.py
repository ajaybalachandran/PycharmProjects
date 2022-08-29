# used to store multiple type of datas
# unchangable
tuple1 = (12, 13, 'hello', 'python')
print(type(tuple1))
print(tuple1)
y = list(tuple1)
print(y)
y.insert(2, 'java')
y[0] = 10
tuple1 = tuple(y)
print(tuple1)
