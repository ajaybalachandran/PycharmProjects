import re
line = 'python programming is fun'
res = re.search('fun', line)
if res:
    print('match found')
else:
    print('match not found')