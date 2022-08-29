f0 = open('new1', 'r')
count = 0
list1 = f0.readlines()
for i in list1:
    count += 1
print(count)