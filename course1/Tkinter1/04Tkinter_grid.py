# in grid do not use pack() method
# assign each element into variable
from tkinter import *
root = Tk()
l1 = Label(root, text='Username:')
l2 = Label(root, text='Password:')
e1 = Entry(root)
e2 = Entry(root)
login = Button(root, text='Login')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
login.grid(row=2, columnspan=2)
root.mainloop()
