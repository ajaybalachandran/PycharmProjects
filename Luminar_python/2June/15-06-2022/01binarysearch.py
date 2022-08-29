def binary_search(list1, key):
    start = 0
    end = len(list1) - 1
    while start <= end:
        mid = (start + end) // 2
        if key < list1[mid]:
            end = mid - 1
        elif key > list1[mid]:
            start = mid + 1
        else:
            return mid
    return -1


lst1 = input('Enter the elements of list: ').split()
res = map(int, lst1)
lst1 = list(res)
lst1.sort()
print(lst1)
k = int(input('Enter teh element you want to search: '))
res = binary_search(lst1, k)
if res == -1:
    print('Item not found')
else:
    print('Item found at index ', res)