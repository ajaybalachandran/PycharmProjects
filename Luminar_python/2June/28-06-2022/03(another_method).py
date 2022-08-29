f1 = open('new2', 'r')
list1 = f1.read()
wordcount = {}
for i in list1.split():
    if i not in wordcount:
        wordcount[i] = 1
    else:
        wordcount[i] += 1
for key, value in wordcount.items():
    print(key, value)