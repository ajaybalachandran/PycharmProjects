from tkinter import *
class MyClass:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        self.l1 = Label(text='STUDENT DETAILS', bg='yellow', fg='black')
        self.l1.pack(fill=X)
        self.l2 = Label(text='Name: Ram')
        self.l2.pack()
        self.l3 = Label(text='Roll No: 01')
        self.l3.pack()
        self.l4 = Label(text='Status: Passed')
        self.l4.pack()
        self.b1 = Button(text='Click', command=self.click_msg)
        self.b1.pack()
        self.b2 = Button(text='Cancel', command=self.cancel_msg)
        self.b2.pack()
        self.b3 = Button(text='Click', command=frame.quit)
        self.b3.pack()
    def click_msg(self):
        print('Clicked')
    def cancel_msg(self):
        print('Canceled')

root = Tk()
obj1 = MyClass(root)
root.mainloop()
