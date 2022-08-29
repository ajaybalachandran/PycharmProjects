dict1 = {}
dict1[1] = 'ajay'
dict1[2] = 'amal'
dict1[3] = 'vimal'
dict1[4] = 'akash'
print(dict1)

dict2 = {5: 'appu', 6: 'ram'}
dict1.update(dict2)
print(dict1)

dict3 = dict2.copy()
print(dict3)

dict4 = dict2
print(dict4)

print(dict4.get(5))

print(dict4[5])

list1 = [1, 2, 3]
print(list1 * 3)