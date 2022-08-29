# n = 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(n, end='')
#     print()

n = 4
res = 0
temp = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(n, end=" ")
        temp = str(n) * j
    res = res + int(temp)
    print()
print("---------------")
print("result", res)
