# List out all the odd numbers from 1 to 100 using lists in Python
oddList = [i for i in range(1, 101) if i == 1 or i % 2 != 0]
print(oddList)