# add(), discard() set functions
set1 = {1, 2, 3, 4}
print(set1)
set2 = {1, 2, 3, 3, 4, 4, 4, 'f'}
set2.add('k')
print(set2)
set2.discard('f')
print(set2)