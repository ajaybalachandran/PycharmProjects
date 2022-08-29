# Handling Button Click
from tkinter import *
root = Tk()
def fun():
    print('clicked')
Button(text='OK', command=fun).pack()

root.mainloop()