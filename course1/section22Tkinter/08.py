# Tkinter using class
from tkinter import *
class MyClass:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        self.pb = Button(frame, text='click', command=self.p_msg)
        self.pb.pack()
        self.qb = Button(frame, text='exit', command=frame.quit)
        self.qb.pack(side=LEFT)
    def p_msg(self):
        print('clicked')
root = Tk()
obj1 = MyClass(root)
# obj2 = MyClass(root)
root.mainloop()
