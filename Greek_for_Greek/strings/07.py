# Input : test_str = ‘geeksforgeek’
# Output : geeksfORGEEK
# Explanation : Latter half of string is uppercased.
#
# Input : test_str = ‘apples’
# Output : appLES
# Explanation : Latter half of string is uppercased.
str1 = input('Enter the string: ')
length = len(str1)
str2 = str1[:(length//2)] + str1[(length//2):].upper()
print(str2)
