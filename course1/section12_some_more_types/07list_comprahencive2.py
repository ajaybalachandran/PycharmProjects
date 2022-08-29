list1 = ['python', 'django', 'flask', 'people']
# new = []
# for i in list1:
#     if 'p' in i:
#         new.append(i)
# print(new)
new = [i for i in list1 if 'p' in i]
print(new)
new = [i.upper() for i in list1]
print(new)