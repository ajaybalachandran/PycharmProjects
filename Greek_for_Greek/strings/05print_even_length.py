# Input: s = "This is a python language"
# Output: This
#               is
#               python
#               language
# Input: s = "i am laxmi"
# Output:     am
str1 = input('Enter the string: ').split()
for i in str1:
    if len(i) % 2 == 0:
        print(i)
