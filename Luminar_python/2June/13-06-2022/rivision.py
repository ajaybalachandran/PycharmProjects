def linear_search(list1, key):
    flag = 0
    for i in list1:
        if i == key:
            flag = 1
            return list1.index(i)
    if flag == 0:
        return -1


lst = input('Enter elements of list: ').split()
int_lst = map(int, lst)
lst = list(int_lst)
k = int(input('Enter the element you want to search: '))
res = linear_search(lst, k)
if res == -1:
    print('Element not found')
else:
    print(f'Element {k} found at index {res}')