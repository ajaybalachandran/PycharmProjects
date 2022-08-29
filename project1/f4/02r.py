# find the number of lines in a file
f1 = open('new1', 'r')
list1 = f1.readlines()
cnt = 0
for i in list1:
    cnt += 1
print('No of lines = ', cnt)