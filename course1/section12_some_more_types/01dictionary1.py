dict1 = {'chair': 500,
         'table': 1000,
         'language': 'python'
         }
# duplication of keys are not allowed
print(dict1['language'])
dict2 = {'chair': 500,
         'chair': 1000,
         'language': 'python'
         }
print(dict2['chair'])  # 1000
# if same key is given then the latest key and value is replace
dict2['sofa'] = 3000  # adding new pair of values
print(dict2)
dict2.update({'chair': 6000})  # another way to add new pair of values
print(dict2)
dict2.pop('chair')  # pops specified item
print(dict2)
dict2.popitem()  # pops last item
print(dict2)
print('----------------------------')
dict3 = {'table': 500,
         'chair': 1000,
         'language': 'python'
         }
for i in dict3.values():
    print(i)