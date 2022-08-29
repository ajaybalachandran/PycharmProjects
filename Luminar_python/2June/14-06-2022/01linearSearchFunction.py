# linear search using function
def linear_search(lis, k):
    n = len(lis)
    for i in range(n):
        if int(lis[i]) == k:
            return i
    return -1


list1 = input('Enter the elements of list: ').split()
print('list is: ', list1)
key = int(input('Enter the element you want to search:'))
res = linear_search(list1, key)
if res == -1:
    print('Item not found')
else:
    print('item found at index', res)
