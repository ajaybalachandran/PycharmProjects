# findall()
import re
line = 'we 23 fgfg 3443 bhbhbh 4343 2'
print(re.findall(r'\d', line))  # digits
print(re.findall(r'\d+', line))  # group of digits
print(re.findall(r'\D', line))  # non digits
