# Given a String, compute all the characters, except spaces.
#
# Input : test_str = ‘geeksforgeeks 33 best’
# Output : 19
# Explanation : Total characters are 19.
#
# Input : test_str = ‘geeksforgeeks best’
# Output : 17
# Explanation : Total characters are 17 except spaces.
str1 = input('Enter the string: ')
cnt = 0
for i in str1:
    if i != ' ':
        cnt += 1
print(cnt)