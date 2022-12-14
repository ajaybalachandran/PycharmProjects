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

toolbar = Frame(root, bg='pink')
toolbar.pack(side=TOP, fill=X)
ins_but = Button(toolbar, text='Crop')
ins_but.pack(side=LEFT, padx=10, pady=5)
ins_but1 = Button(toolbar, text='Run')
ins_but1.pack(side=LEFT, padx=10, pady=5)

statusbar = Label(root, text='this is status bar', relief=SUNKEN, bd=1, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)
root.mainloop()
