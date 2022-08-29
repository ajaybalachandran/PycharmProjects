list1 = input('Enter the elements of Array: ').split()
list1 = list(map(int, list1))
length = len(list1)
k = int(input('Enter the rotation count: '))
count = 0
list2 = []
for i in range(length-1, -1, -1):
    count += 1
    if count > k:
        break
    else:
        list2.append(list1[i])
for j in range(k):
    list1.pop()
print(list2[::-1] + list1)

