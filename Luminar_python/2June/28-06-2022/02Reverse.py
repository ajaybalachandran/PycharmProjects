# print reverse of lines in a txt file
f1 = open('new1', 'r+')
list1 = f1.readlines()
# f1.seek(0)
# f1.writelines(list1[::-1])
# f1.seek(0)
# print(f1.read())
# f1.close()
f1.close()
for i in list1[::-1]:
    print(i.strip())

