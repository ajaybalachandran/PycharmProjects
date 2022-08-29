# Input : str =” geeks quiz practice code”
# Output : str = code practice quiz geeks
# Input : str = “my name is laxmi”
# output : str= laxmi is name my
str1 = input('Enter a string: ')
length = len(str1)
str2 = ''
for i in range(-1, -length-1, -1):
    if str1[i] != ' ':
        str2 = str2 + str1[i]
    if str1[i] == ' ' or str1[i] == str1[0]:
        print(str2[::-1], end=' ')
        str2 = ''
