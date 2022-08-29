f1 = open('new1', 'r')
copy = []
for i in f1:
    copy.append(i)
f1.close()
f2 = open('new3', 'w+')
f2.writelines(copy)
f2.seek(0)
print(f2.read())
f2.close()
