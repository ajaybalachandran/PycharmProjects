# # find the number of words in a file
# f1 = open('new1', 'r')
# str1 = f1.read()
# count = 0
# for i in str1.split():
#     count += 1
# print(count)
f1 = open('new1', 'r')
list1 = f1.read().split()
wordcount = {}
for i in list1:
    if i not in wordcount:
        wordcount[i] = 1
    else:
        wordcount[i] += 1
for key, value in wordcount.items():
    print(key, ':', value)