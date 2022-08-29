f1 = open('new1', 'r')
f2 = open('copy', 'w+')
for i in f1:
    f2.writelines(i)
f1.close()
f2.seek(0)
print(f2.read())
f2.close()