# print the line in text file with the string 'she'
import re
f1 = open('text', 'r')
list1 = f1.readlines()
for i in list1:
    if re.search('she', i):
        print(i)