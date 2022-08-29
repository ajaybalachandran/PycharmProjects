# password valid or not
# length 6-16
#atleast one in a-z, A-Z, 0-9, @#$

import re
password = input('Enter the password: ')
length = len(password)
if not 6 <= length <= 16:
    print('Invalid Password')
elif not re.search('[a-z]', password):
    print('Invalid password')
elif not re.search('[A-Z]', password):
    print('Invalid password')
elif not re.search('[0-9]', password):
    print('Invalid password')
elif not re.search('[@#$]', password):
    print('Invalid password')
else:
    print('valid password')