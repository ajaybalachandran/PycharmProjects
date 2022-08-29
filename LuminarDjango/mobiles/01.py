# 27-07-2022
lst = [1, 2, 3, 4, 'hello', 'hai']
# str_list = [str(data) for data in lst]
# num_list = [data for data in str_list if data.isdigit()]
# number_list = [int(dat) for dat in num_list]
# print(number_list)
number_list = [data for data in lst if isinstance(data, int)]
print(number_list)
