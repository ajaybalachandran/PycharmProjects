list1 = input('Enter the elements: ').split()
res = map(int, list1)
list1 = list(res)
even = filter(lambda i: i % 2 == 0, list1)
print(list(even))
odd = filter(lambda i: i % 2 != 0, list1)
print(list(odd))