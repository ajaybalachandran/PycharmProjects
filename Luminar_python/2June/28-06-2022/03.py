# count the number of words in a file
# f1 = open('new2', 'r')
# list1 = f1.read().split()
# for i in list1:
#     print(i)


f1 = open('new2', 'r')
wordcount = {}
count = 0
list1 = f1.read()
for i in list1.split():
    for j in list1.split():
        if i == j:
            count += 1
    wordcount[i] = count
    count = 0
for key, value in wordcount.items():
    print(key, ':', value)
