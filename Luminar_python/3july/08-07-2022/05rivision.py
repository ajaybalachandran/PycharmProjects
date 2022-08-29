# import re
# line = 'python programming is fun'
# # m = re.match('is', line)
# m = re.match('python', line)
# if m:
#     print('fond')
# else:
#     print('not found')


# import re
# line = 'python programming is fun'
# m = re.search('programming', line)
# if m:
#     print('found')
# else:
#     print('not found')


# import re
# line = 'it is 123 and 456'
# m = re.findall(r'\D', line)  # non digits
# print(m)
# m2 = re.findall(r'\d', line)  # digits
# print(m2)
# m3 = re.findall(r'\d+', line)  # group of digits
# print(m3)


# import re
# zipcode = '1234-5678-9123-4567'
# res1 = re.sub(r'\D', '$', zipcode)
# print(res1)
# res2 = re.sub(r'\d', '@', zipcode)
# print(res2)
# res3 = re.sub(r'\d+', '#', zipcode)
# print(res3)