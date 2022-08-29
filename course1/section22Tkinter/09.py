from tkinter import *
root = Tk()
def undo_msg():
    print('Undo clicked')
my_menu = Menu(root)
root.config(menu=my_menu)
sub_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=sub_menu)
sub_menu.add_command(label='Save1')
sub_menu.add_command(label='Save2')
sub_menu.add_separator()
sub_menu.add_command(label='Save3')
sub_menu.add_command(label='Save4')
new_menu = Menu(my_menu)
my_menu.add_cascade(label='edit', menu=new_menu)
new_menu.add_command(label='Undo', command=undo_msg)
root.mainloop()