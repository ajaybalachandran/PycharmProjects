file1 = open('demo1.txt', 'a+')
file1.write('ajay')
file1.close()
file2 = open('demo1.txt')
print(file2.read())

