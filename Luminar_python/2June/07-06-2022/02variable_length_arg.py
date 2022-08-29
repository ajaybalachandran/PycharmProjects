# variable length argument
# here we can pass any number arguments to the function
def variable_length(*argument):
    for i in argument:
        print(i, end=' ')
# variable_length(10)
# variable_length(10, 20)
variable_length(10, 20, 30, 40)
