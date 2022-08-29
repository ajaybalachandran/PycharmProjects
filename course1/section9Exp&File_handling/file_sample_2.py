file = open('sample2.txt', 'w')  # here w is write mode
file.write('Hai I am inmakes')
file.close()
file = open('sample2.txt', 'a')  # here a is append mode
file.write('\nI am from Kollam')
file.close()
file = open('sample2.txt', 'r')  # here r is read mode
print(file.readline())
print(type(file))
file.close()
