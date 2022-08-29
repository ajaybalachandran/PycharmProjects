from tkinter import *
root = Tk()
def fun1():
    print('hai clicked')
my_menu = Menu(root)
root.config(menu=my_menu)
sub_menu = Menu(my_menu)

my_menu.add_cascade(label='file', menu=sub_menu)

sub_menu.add_command(label='save')
sub_menu.add_command(label='save1')
sub_menu.add_separator()
sub_menu.add_command(label='save2')
sub_menu.add_command(label='save3')

new_menu = Menu(my_menu)

my_menu.add_cascade(label='edit', menu=new_menu)
new_menu.add_command(label='undo', command=fun1)
root.mainloop()
