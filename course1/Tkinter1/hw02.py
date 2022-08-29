# username
# mob
# email
# age
# pass
# confirm pass
# login button
# cancel button
from tkinter import *
root = Tk()
heading = Label(root, text='REGISTRATION FORM')

l1 = Label(root, text='Username:')
l2 = Label(root, text='Mobile no:')
l3 = Label(root, text='Email:')
l4 = Label(root, text='Age:')
l5 = Label(root, text='Password:')
l6 = Label(root, text='Confirm Password:')

b1 = Button(root, text='Login')
b2 = Button(root, text='Cancel')

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)

heading.grid(row=0, columnspan=2)

l1.grid(row=1, column=0)
l2.grid(row=2, column=0)
l3.grid(row=3, column=0)
l4.grid(row=4, column=0)
l5.grid(row=5, column=0)
l6.grid(row=6, column=0)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)

b1.grid(row=7, column=0)
b2.grid(row=7, column=1)

root.mainloop()
