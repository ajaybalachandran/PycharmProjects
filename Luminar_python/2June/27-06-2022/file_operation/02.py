# find the number of lines in a file
fo = open('new', 'r')
count = 0
list1 = fo.readlines()
for i in list1:
    count += 1
fo.close()
print(count)

