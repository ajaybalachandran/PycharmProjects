f1 = open('new1', 'r')
list1 = f1.readlines()
f1.close()
list1 = list1[::-1]
for i in list1:
    print(i.strip())
