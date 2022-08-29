dict1 = {1: 'one', 2: 'two', 3: 'three'}
print(dict1.get(1))
print(dict1.get(2))
print(dict1.get(3))
print(dict1.get(4))
print(dict1.get(4, 'not found'))
print(dict1.get(1, 'found'))