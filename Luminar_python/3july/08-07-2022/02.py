# regular expressions
# match, search fns
import re
line = 'Python programming is fun'
# m = re.match(r'Python', line)  # found
# m = re.match(r'fun', line)  # not found
m = re.search(r'fun', line)
if m:
    print('Match found')
else:
    print('Match not found')