# 11 List Functions
# append, insert, len, index, remove
fruits = ['apple', 'orange', 'pineapple']
fruits.append('cherry')  # adds to the end of list
print(fruits)
fruits.insert(1, 'grapes')
print(fruits)
print(len(fruits))
print(fruits.index('cherry'))
fruits.remove('orange')
print(fruits)
fruits.pop(-1)
print(fruits)
del fruits[0]
print(fruits)
fruits.clear()
print(fruits)
del fruits
try:
    print(fruits)
except:
    print('list is deleted')
