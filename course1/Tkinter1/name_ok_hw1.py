from tkinter import *
root = Tk()
label = Label(root, text='Hello Ajay')
label.pack()
frame1 = Frame(root)
frame1.pack()
button = Button(frame1, text='OK', bg='gray', fg='black')
button.pack()
root.mainloop()
