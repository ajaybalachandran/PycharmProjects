list1 = [22, 33, 22, 'hello', 'python']
# list is ordered, changeable, duplication allowed
print(list1)
print(list1[-1])
print(len(list1))
print(type(list1))
list2 = list(('django', 'flask', 'pyramid'))
print(list1 + list2)
list2[2] = 'angular'
print(list1 + list2)