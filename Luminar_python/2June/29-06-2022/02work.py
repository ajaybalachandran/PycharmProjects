# number of upper case letters, lower case and digits
f1 = open('sample', 'r')
list1 = f1.read()
print(list1)
lc, uc, dc = 0
for i in list1:
    if 48 <= ord(i) <= 57:
        dc += 1
    elif 97 <= ord(i) <= 122:
        lc += 1
    elif 65 <= ord(i) <= 90:
        uc += 1
    else:
        continue
print('No of Upper Case letters = ', uc)
print('No of Lower Case letters = ', lc)
print('No of Digits = ', dc)

