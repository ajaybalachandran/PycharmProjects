# find the even length words in a string
str1 = input('Enter the string: ').split()
for i in str1:
    if len(i) % 2 == 0:
        print(i)