f0 = open('new', 'r')
f1 = open('copyofnew', 'a+')
for i in f0:
    f1.writelines(i)
print(f1.read())
