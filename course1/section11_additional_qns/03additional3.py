# this program will print numbers from 20 to 25 except 22
n = 25
i = 20
while i <= n:
    if i == 22:
        i += 1
        continue
    else:
        print(i)
        i += 1