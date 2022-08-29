import re
line = 'g..d'
if re.match(line, 'good'):
    print('found')
else:
    print('not found')