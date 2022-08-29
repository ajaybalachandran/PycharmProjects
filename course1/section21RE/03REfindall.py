import re
line = 'python is a popular programming language and it is released in 20 feb 1991 and python is '
print(re.findall('is', line))
print(re.findall(r'\D', line))
print(re.findall(r'\d', line))
print(re.findall(r'\d+', line))