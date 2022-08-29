# write
f1 = open('new', 'r+')
f1.write('where are you')
print(f1.tell())  # to display the current file pointer location
f1.seek(0)  # to change the file pointer location
print(f1.readline())

# f1.close()
# f2 = open('new', 'r')
# print(f2.readline())
