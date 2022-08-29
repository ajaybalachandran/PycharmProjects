f1 = open('new', 'r+')
seq = ['First line\n', 'Second line\n', 'Third line\n']
f1.writelines(seq)
f1.seek(0)
print(f1.readlines())
f1.close()