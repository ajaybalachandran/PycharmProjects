# program to find the first recursive letter in a given string
string = input('Enter a string: ')
n = len(string)
res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if string[j] == string[i]:
            res = string[j]
            break
    if res != 0:
        break
if res == 0:
    print('There is no recursive letter in the string')
else:
    print(f'{res} is first recursive')
