f0 = open('new2', 'r+')
f0.write('hi')
f0.seek(0)
content = f0.read()
f0.close()
print(content)