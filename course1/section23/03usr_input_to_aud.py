from gtts import gTTS
import os
from tkinter import *
root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()
def txt_to_speech():
    text=entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save('fileoutput1.mp3')
    os.system('start fileoutput1.mp3')
entry = Entry(root)
canvas.create_window(200, 180, window=entry)
button = Button(text='Start', command=txt_to_speech)
canvas.create_window(230, 230, window=button)
root.mainloop()


