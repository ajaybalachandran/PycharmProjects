# dictionary have keys and values
dict1 = {'one': 'ajay', 'two': 'kollam', 'three': 'kochi', 1: [1, 2, 3]}
# for example in dict1 dictionary 'one' is a key and 'ajay' is its value
# a pair of key and value is called an item [eg --> 'one': 'ajay' is an item in the dictionary
print(type(dict1))
print(dict1)
print(len(dict1))
print(dict1['one'])  # prints the value of key 'one' which is ajay

a = dict1.keys()  # prints all keys in the dictionary
print(a)

a = dict1.values()  # prints all values of the dictionary
print(a)

a = dict1.items()  # prints each items in the dictionary as a pair
print(a)

print(dict1['one'])  # prints the value of key 'one' which is ajay

dict1['four'] = 'ajay'  # adding a new item to the dictionary
print(dict1)

dict1.pop('one')
print(dict1)
