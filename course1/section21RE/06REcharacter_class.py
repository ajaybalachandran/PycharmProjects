import re
pattern = '[A-Z][0-9][a-z]'
line = 'hai i am P8u'
if re.search(pattern, line):
    print('found')
else:
    print('not found')