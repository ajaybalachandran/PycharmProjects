# list is ordered, changeable, duplication allowed

list1 = [25, 50, 'ram', 'Kollam']
print(list1)
print(type(list1))
print(len(list1))
print(list1[-4])
list2 = list((32, 'kochi', 46.44, 'cabbage'))
print(list2)
print(type(list2[0]))
print(list1 + list2)
list2[1] = 'inmakes'
print(list2)