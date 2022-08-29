# Write Python code which accepts name of a product and in turn returns
# their respective prices.

# Make sure to use dictionaries to store products and their respective prices.
# The dictionary should include at least 5 elements
product = {}
n = int(input('Enter the size of dictionary: '))
for i in range(1, n+1):
    key = input(f'enter the key {i}: ')
    value = int(input(f'Enter the value{i}: '))
    product.update({key: value})
print(product)
search = input('Enter the key you want to search: ')
print(product[search])
