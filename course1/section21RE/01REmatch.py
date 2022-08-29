import re
line = 'python programming is fun'
res = re.match('python', line)
# res = re.match('is', line)
if res:
    print('Match found')
else:
    print('Match not found')