list1 = ['apple', 'mango', 'orange', 'pineapple']
print(list1)
# pop function is used for delete an element from the list by using index number
list1.pop(-1)
print(list1)
# append function is used to add an element to the end of the list
list1.append('cherry')
print(list1)
# insert function is used to insert an element to the specified position
# first argument is for index number and second is for the element
list1.insert(0, 'ajay')
print(list1)
# index function is used to find the index number of an item
print(list1.index('orange'))
list1.remove('mango')
print(list1)
list1.pop(0)
print(list1)
list1.clear()
print(list1)
del list1