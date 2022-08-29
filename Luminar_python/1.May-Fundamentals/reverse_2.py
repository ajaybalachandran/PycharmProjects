num = input('Enter a number: ')
length = len(num)
for i in range(length-1, -1, -1):
    if i == length - 1:
        rev = num[i]
        i -= 1
        continue
    else:
        rev = rev + num[i]
print(rev)