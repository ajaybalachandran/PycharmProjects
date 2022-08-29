# Message box
from tkinter import *
from tkinter import messagebox
root = Tk()
# messagebox.showinfo('Info', 'this is my info')
# messagebox.showwarning('warning', 'this is warning')
# messagebox.showerror('Error', 'This is an error')
# messagebox.askquestion('ask', 'do you want to continue')
# messagebox.askokcancel('ask', 'do you want to leave')
# messagebox.askyesno('ask', 'are you sure?')
messagebox.askretrycancel('ask', 'retry or cancel?')
root.mainloop()
