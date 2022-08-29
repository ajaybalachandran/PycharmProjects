# keyword arguments
# def fun(name, age):
#     print('name: ', name)
#     print('age: ', age)
# fun(age = 12, name= 'anu')


def fun(**karg):
    print(type(karg))
    for key, value in karg.items():
        print(key, ':', value)


fun(name='ajay', age=25, cls='bca')