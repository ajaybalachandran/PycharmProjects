brands = ['samsung', 'nokia', 'lg', 'hp']
for item in brands:
    print(item)
    if item == '123':   # if the break statement works then the else block don't execute.
        # otherwise else block will be executed
        break
else:
    print('This is for after else')